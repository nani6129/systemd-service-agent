from .intent_parser import parse_request
from .tools import (
    start_service,
    stop_service,
    restart_service,
    status_service,
    enable_service,
    disable_service,
    list_services,
)

TOOLS = {
    "start": start_service,
    "stop": stop_service,
    "restart": restart_service,
    "status": status_service,
    "enable": enable_service,
    "disable": disable_service,
    "list": list_services,
}

CONFIRMATION_REQUIRED = {"start", "stop", "restart", "enable", "disable"}


def handle_request(request, confirm=False):
    """Process a natural-language or direct service request."""
    if not isinstance(request, str) or not request.strip():
        return {"success": False, "message": "Request must not be empty"}
    parts = request.strip().split()

    if len(parts) == 2 and parts[0].lower() in TOOLS:
        operation, service = parts[0].lower(), parts[1]
    else:
        intent = parse_request(request)
        if intent is None:
            return {"success": False, "message": "Request not understood"}
        operation = intent["operation"]
        service = intent["service"]

    if operation not in TOOLS:
        return {"success": False, "message": "Operation not allowed"}

    if operation in CONFIRMATION_REQUIRED and not confirm:
        return {
            "success": False,
            "operation": operation,
            "service": service,
            "confirmation_required": True,
            "message": "Confirmation required before changing service state",
        }
    if operation == "list":
        result = list_services()
    else:
        result = globals()[f"{operation}_service"](service)
    return {
        **result,
        "operation": operation,
        "service": service,
        "confirmation_required": False,
    }
