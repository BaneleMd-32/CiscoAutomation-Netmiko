# Cisco Router Automation with Netmiko (Python)

This Python script automates basic configuration and verification tasks on a Cisco IOS device using **Netmiko**.  
It connects to a router, configures interfaces, sets up EIGRP, and runs several verification commands.

---

## Features:

- Connects to a Cisco router via SSH
- Configures interface `GigabitEthernet0/2`
- Sets up EIGRP routing
- Loads additional configuration from a file (`prep3_2.txt`)
- Executes `show` commands to verify configuration and connectivity
- Handles connection, authentication, and general exceptions

---

## Requirements:

- Python 3.8+ installed
- Netmiko library installed (`pip install netmiko`)
- SSH access to a Cisco IOS device
- A configuration file (`prep3_2.txt`) with additional CLI commands

