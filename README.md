# Systemd Service Agent

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

## Requirements

- Linux with systemd
- Python 3.10 or newer
- systemctl

## Setup

Clone the repository, then enter the project directory:

```bash
cd systemd-service-agent
python3 -m systemd_agent.agent
