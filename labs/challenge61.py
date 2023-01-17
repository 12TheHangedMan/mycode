#!/usr/bin/env python3

# extra credit 01
userinput = input("enter count down yourself")

# extra credit 02
try:
    if userinput == "":
        converted_input = 99
    else:
        converted_input = int(userinput)
except:
    print("invalid input, enter must be a number")
else:
    if converted_input > 100:
        print("invalid input, enter must be smaller than 100")
    else:
        for i in range(converted_input - 1):
            print(f"{converted_input-i} bottles of beer on the wall!")
            print(f"{converted_input-i} bottles of beer on the wall! {converted_input-i} bottles of beer! You take one down, pass it around!")

