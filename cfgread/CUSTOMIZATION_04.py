#!/usr/bin/env python3
## create file object in "r"ead mode


userinput = input("Please indicate the name of the file(to also include the file type, file.cfg for example)")

if userinput == "":
    userinput = "vlanconfig.cfg"

try:
    with open(userinput, "r") as configfile:
        ## readlines() creates a list by reading target
        ## file line by line
        configlist = configfile.readlines()

    ## file was just auto closed (no more indenting)
except: 
    print("very likely no such file exists")
else:
    ## each item of the list now has the "\n" characters back
    print(configlist)

