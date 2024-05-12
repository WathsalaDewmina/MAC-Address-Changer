#!/usr/bin/python3

import subprocess
import optparse
import re

def change_mac_address(interface, new_mac):
    # Disable the interface
    subprocess.call(["ifconfig", interface, "down"])
    # Change the MAC address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    # Enable the interface
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changing MAC Address of Interface {} to {}".format(interface, new_mac))

def get_arguments():
    # Create an OptionParser object
    parser = optparse.OptionParser()
    # Define command line options
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    # Parse command line arguments
    (options, arguments) = parser.parse_args()

    # Check if interface and new MAC address are provided
    if not options.interface:
        parser.error("[-] Please specify an interface. Use python macchanger --help for more details.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address. Use python macchanger --help for more details.")

    return options

def get_current_mac(interface):
    # Get current MAC address of the interface
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # Extract MAC address using regex
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8'))

    if current_mac:
        return current_mac.group(0)
    else:
        return None

# Get command line arguments
options = get_arguments()

# Change MAC address
change_mac_address(options.interface, options.new_mac)

# Get final MAC address
final_mac = get_current_mac(options.interface)

# Verify whether the MAC address is changed or not
if final_mac == options.new_mac:
    print("MAC Address successfully changed to {}".format(final_mac))
else:
    print("Error occurred while changin the MAC address, please check your MAC Address is valid")
    print("Sample MAC address format:\n00:11:22:33:44:55")
