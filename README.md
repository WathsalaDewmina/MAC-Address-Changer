# MAC Address Changer

## Why MAC Address Changing is Important in Cyber Security Related Activities

Changing MAC addresses can be an essential aspect of cyber security-related activities as it can help in maintaining anonymity, bypassing MAC address-based filters, and avoiding tracking. By altering your MAC address, you can make it harder for adversaries to trace your network activity back to your device, enhancing your privacy and security.

## What is MAC Address?

A Media Access Control (MAC) address is a unique identifier assigned to a network interface controller (NIC) for communications at the data link layer of a network segment. It serves as a hardware address for devices in a network.

<img src="macchanger_screenshot.png" alt="MAC Address Changer Screenshot" width="600"/>

## Steps

1. **Download the Source Code:**
    - Clone the repository to your local machine using the following command:
        ```sh
        git clone https://github.com/WathsalaDewmina/MAC-Address-Changer.git
        ```

2. **Navigate to the Project Directory:**
    - Open a terminal/command prompt and navigate to the directory where you downloaded the source code.

3. **Running the Script:**

    - Execute the following command in your terminal to run the script:
        ```sh
        python3 macchanger.py -i <interface> -m <new_mac>
        ```

    - Replace `<interface>` with the name of your network interface (e.g., eth0, wlan0) and `<new_mac>` with the new MAC address you want to assign.

### Examples

Change MAC address of interface eth0 to 00:11:22:33:44:55:

```sh
python3 macchanger.py -i eth0 -m 00:11:22:33:44:55
python3 macchanger.py -i wlan0 -m 12:34:56:78:9A:BC
