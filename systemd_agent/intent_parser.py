import re

OPERATIONS = {
    "start", "stop", "restart",
    "status", "enable", "disable",
}


def parse_request(request):
    """Parse a simple natural-language service request into an intent."""
    if not isinstance(request, str) or not request.strip():
        return None

    text = request.lower().strip()

    # Reject unrelated or explicitly destructive requests.
    blocked = (
        "delete everything",
        "erase the disk",
        "format the drive",
        "remove all files",
    )
    if any(phrase in text for phrase in blocked):
        return None

    # Identify the requested operation.
    if re.search(r"\b(disable|turn off)\b", text):
        operation = "disable"
    elif re.search(
        r"\b(enable|automatically start|start on boot|"
        r"start at boot|at boot|on boot)\b", text
    ):
        operation = "enable"
    elif re.search(r"\b(restart|reboot)\b", text):
        operation = "restart"
    elif re.search(r"\b(stop|shut down)\b", text):
        operation = "stop"
    elif re.search(r"\b(start|launch)\b", text):
        operation = "start"
    elif re.search(
        r"\b(status|running|active|check|show)\b", text
    ):
        operation = "status"
    else:
        return None

    # Prefer a service name explicitly following "service" or "daemon".
    match = re.search(
        r"\b(?:service|daemon)\s+([a-zA-Z0-9_.@:-]+)\b",
        text,
    )

    if match:
        service = match.group(1)
    else:
        # Remove common instruction words, then identify a candidate.
        words = re.findall(r"[a-zA-Z0-9_.@:-]+", text)
        ignored = {
            "please", "check", "whether", "if", "is", "are",
            "the", "a", "an", "my", "me", "tell", "show",
            "get", "find", "make", "sure", "that", "and",
            "automatically", "start", "stop", "restart",
            "reboot", "status", "enable", "disable", "active",
            "running", "currently", "now", "at", "on", "boot",
            "computer", "system", "turn", "off", "up", "launch",
            "shut", "down", "service", "daemon",
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
