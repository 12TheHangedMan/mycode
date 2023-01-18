#!/usr/bin/env python3
import math

zodiac1 = {
    0: "Rat",
    1: "Ox",
    2: "Tiger",
    3: "Rabbit",
    4: "Dragon",
    5: "Snake",
    6: "Horse",
    7: "Sheep",
    8: "Monkey",
    9: "Rooster",
    10: "Dog",
    11: "Pig"
}

zodiac2 = {
    "Rat": "artistic, sociable, inducharming, charming and intelligent",
    "Ox": "strong, thorough, determined, loyal, and reliable",
    "Tiger": "courageous, enthusiastic, confident, charismatic, and a leader",
    "Rabbit": "vigilant, witty, quick-minded, and ingenious",
    "Dragon": "talented, powerful, lucky, and successfull",
    "Snake": "wise, like to work alone, and determined",
    "Horse": "animated, active, and energetic",
    "Sheep": "creative, resilient, gentle, mild-mannered, and shy",
    "Monkey": "sharp, smart, curious, and mischievious",
    "Rooster": "hardworking, resourceful, courageous, and talented",
    "Dog": "you are loyal, honest, cautious, and kind",
    "Pig": "a symbol of wealth, honesty, and practicality"
}


def main():
    usr_name = input("Please enter your name:\n>").lower().title()

    try:
        usr_date = input(
            "Please enter your birth year in YYYY format, e.g 2010:\n>")
        usr_date = int(usr_date)
    except:
        print("enter a valid number please")
    else:
        z_key = (usr_date - 1960) % 12

        usr_zodiac = zodiac1[z_key]
        usr_charactor = zodiac2[usr_zodiac]

        print(f"{usr_name} your zodiac sign is {usr_zodiac}, you are {usr_charactor}.")


if __name__ == "__main__":
    main()

