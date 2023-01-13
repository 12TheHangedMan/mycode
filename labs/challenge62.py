#!usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def part3(farm_name):
    for farm in farms:
        if farm.get("name") == farm_name:
            for animal in farm.get("agriculture"):
                if(animal != "carrorts" and animal != "celery")
                print(animal)

#part2
def part2(farm_name):
    for farm in farms:
        if farm.get("name") == farm_name:
            for animal in farm.get("agriculture"):
                print(animal)

def part1():
    for farm in farms:
        if farm.get("name") == "NE Farm":
            for animal in farm.get("agriculture"):
                print(animal)

def main():
    user_input = "choose a farm from NE Farm, W Farm, SE Farm"
    validated_input = user_input.lower().split();
    if(validated_input == "ne farm"):
        part2("NE Farm")
    elif(validated_input == "w farm"):
        part2("W Farm")
    elif(validated_input == "se farm"):
        part2("SE Farm")
    else:
        print("invalid input")


if __name__ == "__main__":
    main()
