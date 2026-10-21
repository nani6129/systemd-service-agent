import re
import subprocess

ALLOWED_OPERATIONS = {
    "start", "stop", "restart",
    "status", "enable", "disable",
}


def validate_service_name(service):
    return (
        isinstance(service, str)
        and bool(re.fullmatch(r"[A-Za-z0-9_.@:-]+", service))
        and not service.startswith("-")
    )


def run_service_operation(operation, service):
    if operation not in ALLOWED_OPERATIONS:
        return {"success": False, "message": "Operation not allowed"}

    if not validate_service_name(service):
        return {"success": False, "message": "Invalid service name"}

    try:
        result = subprocess.run(
            ["systemctl", operation, service],
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
        output = (result.stdout + result.stderr).strip()

        return {
            "success": result.returncode == 0,
            "operation": operation,
            "service": service,
            "return_code": result.returncode,
            "message": output or (
                "Operation completed"
                if result.returncode == 0
                else "Operation failed"
            ),
        }
    except FileNotFoundError:
        return {"success": False, "message": "systemctl not found"}
    except subprocess.TimeoutExpired:
        return {"success": False, "message": "Operation timed out"}


def start_service(service):
    return run_service_operation("start", service)


def stop_service(service):
    return run_service_operation("stop", service)


def restart_service(service):
    return run_service_operation("restart", service)


def status_service(service):
    return run_service_operation("status", service)


def enable_service(service):
    return run_service_operation("enable", service)


def disable_service(service):
    return run_service_operation("disable", service)
