#!/usr/bin/env python3
count = 0
vampirelines = []

with open("../../dracula.txt", "r") as Dracula:
    for line in Dracula:
        if "vampire" in line.lower():
            print(line)
            count += 1
            vampirelines.append(line)

with open("vampytimes.txt", "w") as vampire:
    for line in vampirelines:
        vampire.write(line)

print(count)
