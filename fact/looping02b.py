#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'"""

with open("dnsservers.txt", "r") as dnsfile:
    dnslist = dnsfile.read()
    for svr in dnslist:
        print(svr, end="")


