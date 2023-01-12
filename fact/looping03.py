#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across range() to generate n UUIDs"""

# standard library import
# allows us to generate UUIDs

import uuid

howmany = 0

try:
    howmany = int(input("How many UUIDs should be generated?"))
except ValueError:
    print("invalid input")
else:
    print("Generating UUIDs...")

for rando in range(howmany):
    print(uuid.uuid4()) # each time through the loop produce a UUID
