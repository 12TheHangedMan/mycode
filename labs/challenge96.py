#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import json


def main():
    selected_amount = random.randint(3, 10)

    # fakeurl = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"

    category = {"general knowledge": "9", "Entertainment: Books": "10", "Entertainment: Music": "11",
                "Entertainment: Musical & Theatres": "12", "Entertainment: Television": "13", "Entertainment: Video Games": "14",
                "Entertainment: Board Games": "15", "Science & Nature": "16", "Science: Computers": "17",
                "Science: Mathmatics": "18", "Mythology": "19", "Sports": "20", "Geography": "21", "History": "22",
                "Politics": "23", "Art": "24", "Celebrities": "25", "Animals": "26"}

    difficulty = {"1": "easy", "2": "medium", "3": "hard"}
    types = {"1": "multiple", "2": "boolean"}

    url1 = f"https://opentdb.com/api.php?amount={selected_amount}"

    # 1. category module
    print("Please select category:")
    for i in range(len(category)):
        print(f"{i+1}. {list(category.keys())[i]}")

    user_select_category = input(f"Please select 1 to {len(category)}")

    url3 = ""
    try:
        select_index = int(user_select_category)
    except:
        print("invalid input, will assign a random category")
    else:
        if select_index < 1 or select_index > len(category):
            print("selection out of range, will assign a random category")
        else:
            select_category = list(category.keys())[select_index]
            select_category_value = category[select_category]
            print(f"You selected {select_category_value}")

            url3 = f"category={select_category_value}"

    # 2. difficulty module
    print("Please select difficulty:")
    for i in range(len(difficulty)):
        print(f"{i+1}. {list(difficulty.values())[i]}")

    user_select_difficulty = input(f"Please select 1 to {len(difficulty)}")
    select_difficulty_value = difficulty.get(user_select_difficulty)

    url4 = ""
    if select_difficulty_value == None:
        print("Invalid input, will assign a random difficulty level")
    else:
        print(f"You selected {select_difficulty_value}")
        url4 = f"difficulty={select_difficulty_value}"

    # 3. type module
    print("Please select question type:")
    for i in range(len(types)):
        print(f"{i+1}. {list(types.values())[i]}")

    user_select_type = input(f"Please select 1 to {len(types)}")
    select_type_value = types.get(user_select_type)

    url5 = ""
    if select_type_value == None:
        print("Invalid input, will assign a random question type")
    else:
        print(f"You selected {select_type_value}")
        url5 = f"type={select_type_value}"

    if url3 != "":
        url3 = "&" + url3
    if url4 != "":
        url4 = "&" + url4
    if url5 != "":
        url5 = "&" + url5

    URL = url1 + url3 + url4 + url5
    # data will be a python dictionary rendered from your API link's JSON!

    data = requests.get(URL).json()

    if data["response_code"] == 0:
        results = data["results"]

        question_index = 1

        while question_index <= selected_amount:
            the_question = results[question_index-1]
            print(f"({question_index}). " +
                  f"{the_question['question']}")

            correct_answer = the_question['correct_answer']
            incorrect_answer = the_question['incorrect_answers']

            answers = incorrect_answer
            answers.append(correct_answer)

            answers = randomize(answers)
            answers_dict = {}

            j = 0
            for answer in answers:
                print(f"{j+1}. {answer}")
                j += 1
                answers_dict[f"{j}"] = answer

            user_input = input("Choose from the answers, select 1, 2, ...")

            if answers_dict.get(user_input) == correct_answer:
                print("correct")
            else:
                print("incorrect")

            question_index += 1


def randomize(lists):
    for i in range(len(lists)):
        random_index = random.randint(0, len(lists)-1)

        temp = lists[i]
        lists[i] = lists[random_index]
        lists[random_index] = temp

    return lists


if __name__ == "__main__":
    main()

