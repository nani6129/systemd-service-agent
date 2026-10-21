import re

OPERATIONS = {
    "start", "stop", "restart",
    "status", "enable", "disable","lisr",
}

def parse_request(request):
    """Parse a natural-language service request into an approved intent."""
    if not isinstance(request, str) or not request.strip():
        return None

    text = request.lower().strip()

    blocked = (
        "delete everything", "erase the disk",
        "format the drive", "remove all files",
    )
    if any(phrase in text for phrase in blocked):
        return None

    # Identify the operation, prioritizing specific phrases.
    if re.search(r"\b(disable|turn off)\b", text):
        operation = "disable"
    elif re.search(
        r"\b(enable|automatically start|start automatically|"
        r"start on boot|start at boot|starts automatically|"
        r"when the computer boots|at boot|on boot)\b", text
    ):
        operation = "enable"
    elif re.search(r"\b(restart|reboot)\b", text):
        operation = "restart"
    elif re.search(r"\b(stop|shut down)\b", text):
        operation = "stop"
    elif re.search(r"\b(start|launch)\b", text):
        operation = "start"
    elif re.search(
        r"\b(list|show)\b.*\b(services|service units)\b"
        r"|\b(list|show)\s+(all\s+)?services\b",
        text,
    ):
        operation = "list"
    elif re.search(
        r"\b(status|running|active|check|show|display)\b",
        text,
    ):
        operation = "status"
    else:
        return None
    # Handle listing services without requiring a service name.
    if operation == "list":
        return {"operation": "list", "service": "all"}
    # Prefer the service name after "service" or "daemon".
    match = re.search(
        r"\b(?:service|daemon)\s+([a-zA-Z0-9_.@:-]+)",
        text,
    )
    if match:
        service = match.group(1)
    else:
        words = re.findall(r"[a-zA-Z0-9_.@:-]+", text)
        ignored = {
            "please", "check", "whether", "if", "is", "are",
            "the", "a", "an", "me", "my", "tell", "find", "of",
            "get", "make", "sure", "that", "and", "when",
            "computer", "boots", "boot", "automatically",
            "start", "starts", "started", "stop", "stops",
            "restart", "reboot", "enable", "enabled",
            "disable", "disabled", "status", "running",
            "active", "currently", "now", "on", "at", "up",
            "show", "display", "turn", "off", "shut", "down",
            "service", "daemon", "launch", "whether",
            "automatically",
            "list", "all", "services", "units",
        }
        candidates = [
            word for word in words
            if word not in ignored and word not in OPERATIONS
        ]
        if not candidates:
            return None
        service = candidates[0]

    if not re.fullmatch(r"[A-Za-z0-9_.@:-]+", service):
        return None

    return {"operation": operation, "service": service}
