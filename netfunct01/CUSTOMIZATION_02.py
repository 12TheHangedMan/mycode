#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# function to reboot devices
def devicereboot(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'connecting to...{ip}') # fstring
        print(f'REBOOTING NOW')
    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    devicereboot(devicecmd) # call function to push commands to devices

# call our main function
if __name__ == "__main__":
    main()

