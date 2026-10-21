# Systemd Service Agent

An Operating Systems project that provides a Python terminal interface for managing Linux services through `systemctl`.

## Objectives
- Manage Linux services from a terminal.
- Start, stop, restart, and check service status.
- Enable or disable services at system boot.
- Validate service names and permitted operations.
- Handle command errors and test the implementation.

## System Architecture

```text
User
  |
  v
Terminal Interface (agent.py)
  |
  v
Operation Dispatcher
  |
  v
Systemd Service Tools (tools.py)
  |
  v
Input Validation
  |
  v
Python subprocess
  |
  v
systemctl
  |
  v
systemd Manager
  |
  v
Linux Services
  |
  v
Result returned to Terminal
```

## Technologies
- Python 3
- Linux and systemd
- systemctl
- subprocess
- unittest
- Git and GitHub

## Project Structure

```text
systemd-service-agent/
├── systemd_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── tools.py
├── tests/
│   └── test_validation.py
├── .gitignore
└── README.md
```

## How to Run

```bash
python3 -m unittest discover -s tests -v
python3 -m systemd_agent.agent
```

Example commands supported by the current terminal interface:

```text
status cron
start cron
stop cron
restart cron
enable cron
disable cron
exit
```

## Testing

The validation test suite checks service-name validation, rejection of unsupported operations, and status handling.

## Future Enhancement

Integrate the service agent with the class-wide Agentic Shell and an LLM so users can request service operations in natural language.

## Author

K. Nani Babu

Operating Systems Project — Systemd Service Agent
