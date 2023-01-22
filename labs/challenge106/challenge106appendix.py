import random
import requests
import json


def generate_question():
    amount = 10
    fakeurl = f"https://opentdb.com/api.php?amount={amount}"

    response = requests.get(fakeurl).json()
    results = response.get("results")
    questions_list = []

    if len(results) > 0:
        for result in results:
            question = result.get("question")
            correct_answer = result.get("correct_answer")
            incorrect_answers = result.get("incorrect_answers")
            incorrect_answers.append(correct_answer)

            answers_list = randomize(incorrect_answers)
            questions_list.append(
                {"question": question, "answers_list": answers_list, "correct_answer": correct_answer})

    return questions_list


def randomize(lists):
    for i in range(len(lists)):
        random_index = random.randint(0, len(lists)-1)

        temp = lists[i]
        lists[i] = lists[random_index]
        lists[random_index] = temp

    return lists
