on# Systemd Service Agent

An Operating Systems project that provides a Python terminal interface
for managing Linux services through systemctl.

## Features

- Check service status
- Start and stop services
- Restart services
- Enable and disable services at boot
- Validate service names and allowed operations
- Confirm state-changing operations
- Capture command output and errors
- Automated unit tests
- Accept simple natural-language service requests
- Parse requests into approved operations and service names

## Requirements

- Linux with systemd
- Python 3.10 or newer
- systemctl

## Setup

Clone the repository, then enter the project directory:

```bash
cd systemd-service-agent
python3 -m systemd_agent.agent
python3 -m systemd_agent.agent
