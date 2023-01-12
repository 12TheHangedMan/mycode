#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Solution to Customization 01"""

# parse keystone.common.wsgi and return number of failed login attempts

loginfail = 0
loginsuccess = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
        if "-] Authorization failed" in line:
            loginsuccess += 1

print("The number of failed log in attempts is", loginfail)
print("The number of successful log ins is", loginsuccess)

