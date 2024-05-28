#!/usr/bin/python3

import subprocess
import optparse
import re
import sys

welcome_screen = r"""

  __  __          _____    _____ _    _          _   _  _____ ______ _____
 |  \/  |   /\   / ____|  / ____| |  | |   /\   | \ | |/ ____|  ____|  __ \
 | \  / |  /  \ | |      | |    | |__| |  /  \  |  \| | |  __| |__  | |__) |
 | |\/| | / /\ \| |      | |    |  __  | / /\ \ | . ` | | |_ |  __| |  _  /
 | |  | |/ ____ \ |____  | |____| |  | |/ ____ \| |\  | |__| | |____| | \ \
 |_|  |_/_/    \_\_____|  \_____|_|  |_/_/    \_\_| \_|\_____|______|_|  \_\

Made By :- Wathsala Dewmina
GitHub  :- https://github.com/WathsalaDewmina/

"""

print(welcome_screen)


# Mac Address Changing function
def change_mac_address(interface, new_mac):
    try:
        # Disable the interface
        subprocess.run(["ifconfig", interface, "down"], check=True)
        # Change the MAC address
        subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], check=True)
        # Enable the interface
        subprocess.run(["ifconfig", interface, "up"], check=True)
        print("[+] Changing MAC Address of Interface {} to {}".format(interface, new_mac))
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to change MAC address: {e}")
        sys.exit(1)


# Taking all the arguments from the user
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
        parser.error("[-] Please specify an interface. Use --help for more details.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address. Use --help for more details.")

    return options


# Getting the current Mac Address of the user using regex
def get_current_mac(interface):
    try:
        # Get current MAC address of the interface
        ifconfig_result = subprocess.check_output(["ifconfig", interface])
        # Extract MAC address using regex
        current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8'))

        if current_mac:
            return current_mac.group(0)
        else:
            print("[-] Could not read MAC address.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[-] Could not get MAC address for interface {interface}: {e}")
        sys.exit(1)


# Validating the mac address
def validate_mac(mac):
    if re.match(r"^(\w\w:){5}\w\w$", mac):
        return True
    else:
        return False


# Checking if the user has root previlages
def check_root():
    if not (os.geteuid() == 0):
        print("[-] This script requires root privileges. Please run as root.")
        sys.exit(1)


# Checking the interface is correct
def check_interface(interface):
    try:
        subprocess.check_output(["ifconfig", interface])
    except subprocess.CalledProcessError:
        print(f"[-] Interface {interface} does not exist.")
        sys.exit(1)


# Performing all the functions orderly
if __name__ == "__main__":
    import os

    # Check for root privileges
    check_root()

    # Get command line arguments
    options = get_arguments()

    # Validate MAC address
    if not validate_mac(options.new_mac):
        print("[-] Invalid MAC address format.")
        print("Sample MAC address format: 00:11:22:33:44:55")
        sys.exit(1)

    # Check if the interface exists
    check_interface(options.interface)

    # Get current MAC address
    current_mac = get_current_mac(options.interface)
    print(f"Current MAC: {current_mac}")

    # Change MAC address
    change_mac_address(options.interface, options.new_mac)

    # Get final MAC address
    final_mac = get_current_mac(options.interface)

    # Verify whether the MAC address is changed or not
    if final_mac == options.new_mac:
        print(f"[+] MAC Address successfully changed to {final_mac}")
    else:
        print("[-] Error occurred while changing the MAC address. Please check if the provided MAC address is valid.")
