from scapy.all import *
import subprocess
import ipaddress  # Library for IP address validation

# Function to check if the IPv6 address is valid and within the specified range
def is_valid_ipv6(new_ip):
    try:
        # Validate IPv6 format
        ip = ipaddress.IPv6Address(new_ip)

        # Define the network range
        network = ipaddress.IPv6Network("fd53:abcd:1234:5::/64", strict=False)

        # Check if the address belongs to the range
        if ip in network:
            return True
        else:
            print(f"IPv6 {new_ip} is not in the fd53:abcd:1234:5::/64 range.")
            return False
    except ipaddress.AddressValueError:
        print(f"IPv6 {new_ip} is invalid.")
        return False

# Function to process and change the IPv6 address of the device (Raspberry Pi)
def change_ip(new_ip):
    if not is_valid_ipv6(new_ip):
        print("IPv6 address change aborted.")
        return

    print(f"Changing IPv6 to: {new_ip}")
    
    # Remove the current IPv6 address (if any)
    remove_command = "ip -6 addr flush dev vlan5"
    try:
        subprocess.run(remove_command, shell=True, check=True)
        print("Successfully removed old IPv6 addresses.")
    except subprocess.CalledProcessError as e:
        print(f"Error removing old IPv6 addresses: {e}")
    
    # Use the 'ip' command to change the IPv6 address
    command = f"ip -6 addr add {new_ip}/64 dev vlan5"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully changed IPv6 to: {new_ip}")
    except subprocess.CalledProcessError as e:
        print(f"Error changing IPv6: {e}")

# Callback function to process captured packets
def packet_callback(pkt):
    print('New packet captured:', pkt)
    
    if Dot1Q in pkt and pkt[Dot1Q].vlan == 25:
        print("Captured packet:")
        pkt.show()
        
        # Extract and print the payload of the Raw layer
        if Raw in pkt:
            load_data = pkt[Raw].load
            try:
                new_ipv6 = load_data.decode().strip()  # New IPv6 address
                change_ip(new_ipv6)
            except UnicodeDecodeError:
                print("Failed to decode the packet payload.")
        else:
            print("No Raw layer found.")

# Listen for packets on the 'vlan5' interface
sniff(iface="vlan5", prn=packet_callback)
