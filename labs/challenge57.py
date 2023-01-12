import html
import random

trivia = {
  "category":
  "Entertainment: Film",
  "type":
  "multiple",
  "question":
  "Which of the following is NOT a quote from the 1942 film Casablanca? ",
  "correct_answer":
  "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
  "incorrect_answers": [
    "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
    "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
    "&quot;Round up the usual suspects.&quot;"
  ]
}


def main():
  print(html.unescape(trivia["question"]))

  answerList = [
    html.unescape(trivia["correct_answer"]),
    html.unescape(trivia["incorrect_answers"][0]),
    html.unescape(trivia["incorrect_answers"][1]),
    html.unescape(trivia["incorrect_answers"][2])
  ]

  count = 0
  title = "A"

  newList = []

  while len(answerList) > 0:

    if (count == 1):
      title = "B"
    elif (count == 2):
      title = "C"
    elif (count == 3):
      title = "D"

    obj = random.choice(answerList)
    answerList.remove(obj)

    newList.append(obj)

    print(f"{title}. {obj}" + "\n")

    count += 1

  inputAnswer = input("Please select from A, B, C, D")

  answerDic = {
    "A": newList[0],
    "B": newList[1],
    "C": newList[2],
    "D": newList[3]
  }

  answer = answerDic.get(inputAnswer.upper(), None)

  if not answer is None and answer == html.unescape(trivia["correct_answer"]):
    print("Correct")
  else:
    print("Incorrect")
    res = input("wanna do again?Y/N")

    if res.upper() == "Y":
      main()


if __name__ == "__main__":
  main()

