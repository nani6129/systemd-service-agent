from .tools import (
    start_service,
    stop_service,
    restart_service,
    status_service,
    enable_service,
    disable_service,
)

TOOLS = {
    "start": start_service,
    "stop": stop_service,
    "restart": restart_service,
    "status": status_service,
    "enable": enable_service,
    "disable": disable_service,
}


def main():
    print("Systemd Service Agent")
    print("Format: <operation> <service>")
    print("Operations:", ", ".join(TOOLS))
    print("Type 'exit' to quit.")

    while True:
        try:
            request = input("Agent > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if request.lower() == "exit":
            break

        parts = request.split()
        if len(parts) != 2:
            print("Use: <operation> <service>")
            continue

        operation, service = parts
        tool = TOOLS.get(operation.lower())

        if tool is None:
            print("Unknown operation.")
            continue

        if operation.lower() in {
            "start", "stop", "restart", "enable", "disable"
        }:
            confirm = input(
                f"Confirm '{operation} {service}'? [y/N]: "
            ).strip().lower()

            if confirm != "y":
                print("Cancelled.")
                continue

        result = tool(service)
        print("SUCCESS" if result["success"] else "FAILED")
        print(result.get("message", "No output"))


if __name__ == "__main__":
    main()
