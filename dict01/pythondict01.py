#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""

    ## create a dictionary with 4 key:value pairs
    switch = {
                "hostname": "sw1",
                "ip":"10.0.1.1",
                "version": "1.2",
                "vendor": "cisco"
            }

    ## display the entire dictionary
    print(switch)

    ## proove that switch is indeed a dictionary
    print(type(switch))
    
    ## display parts of the dictionary
    print(switch["hostname"])
    print(switch["ip"])

    ## request a 'fake' key
    # this will cause the program to FAIL 
    print(switch["lynx"])

# call our main function
if __name__ == "__main__":
        main()
