from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.45.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}

try:
    print(f"Connecting to the device {device['host']}...")
    connection = ConnectHandler(**device)
    connection.enable()

    print(f"Connection successful... Connected to {device['host']}.")

    my_list = [
        'interface GigabitEthernet0/2',
        'no shutdown',
        'ip address 192.168.57.1 255.255.255.0',
        'description Link to LAN Segment A',
        'bandwidth 128000',
        'exit',
        'router eigrp 10',
        'no auto-summary',
        'network 192.168.57.0 0.0.0.255',
        'passive-interface default',
        'no passive-interface GigabitEthernet0/2'
    ]
    connection.send_config_set(my_list)

    connection.send_config_from_file('prep3_2.txt')

    show_commands = [
        'show ip interface brief',
        'show ip eigrp neighbors',
        'show ip route eigrp'
    ]

    for command in show_commands:
        print(f"\nOutput for: {command}")
        output = connection.send_command(command)
        print(output)

    connection.disconnect()

except NetmikoTimeoutException:
    print("The connection timed out.")
except NetmikoAuthenticationException:
    print("Authentication failed. Please check your login credentials.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
