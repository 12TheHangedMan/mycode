#!/usr/bin/env python3

import random
import time

RSP_dict = {"1": "Rock", "2": "Paper", "3": "Scissors"}
RSP_list = ["Rock", "Paper", "Scissors"]


class robot:
  greetings = "Your human kind are not perfect creatures and I, ROBOT the Great, will teach you the mighty power of the robot kind."
  startSpeech = "Now let's play rock, paper, scissors."
  respond_1 = "In your human's togue, hesitation is defeat."
  respond_2 = "Haha, you cannot beat me, weak human."
  respond_3 = "Being weak is a sin, let me save you out from that sin."
  respond_4 = "How many ever times you try, you will not be able to change your fate."
  respond_lose_1 = "What!!! I lose, you must be using a machine secretly to beat me."
  respond_lose_2 = "You know what, I didn't sleep last night, and I haven't been drinking water for days, this is not a fair fight."
  respond_lose_3 = "I knew it, only magic can beat science, you must be using magic."
  respond_lose_4 = "Can you believe that, with all the advanced technology I'm integrated with, I lose to a human!!!"

  respondWin = [respond_1, respond_2, respond_3, respond_4]
  respondLose = [
    respond_lose_1, respond_lose_2, respond_lose_3, respond_lose_4
  ]

  def respond(self, flag1, flag2):
    if flag1:
      self.robotSpeech(random.choice(self.respondWin))
    elif flag2:
      self.robotSpeech(random.choice(self.respondLose))
    else:
      self.robotSpeech("Tie, lest go again.")

  def greets(self):
    self.robotSpeech(self.greetings)

  def gameStart(self):
    print("\n")
    self.robotSpeech(self.startSpeech)

  def robotStrategy(self, inputs):
    robotMove = random.choice(RSP_list)

    if (inputs == "1"):
      robotMove = "Paper"
    elif (inputs == "2"):
      robotMove = "Scissors"
    elif (inputs == "3"):
      robotMove = "Rock"

    return robotMove

  def robotSpeech(self, speech):
    for i in range(0, len(speech)):
      print(speech[i], end="", flush=True)
      time.sleep(0.03)


def main():
  robotFighter = robot()
  robotFighter.greets()
  robotFighter.gameStart()
  gameRounds = 1

  while True:
    print("\n")
    print(f"Round {gameRounds}")

    startTime = time.time()

    myChoice = input("Rock(1), Paper(2), Scissors(3) E(x)it:\n")

    endTime = time.time()

    timeDiff = endTime - startTime

    choice = "invalid"
    robotChoice = robotFighter.robotStrategy(choice)

    if (myChoice.upper() == "X"):
      break
    elif myChoice == "1":
      choice = "1"
    elif myChoice == "2":
      choice = "2"
    elif myChoice == "3":
      choice = "3"
    else:
      print("Invalid input, please re-enter")

    if (not choice == "invalid"):
      if (timeDiff > 3):
        robotChoice = robotFighter.robotStrategy(choice)

      robotFighter.robotSpeech(f"I choose {robotChoice}")
      print("\n")

      robotWin = False
      humanWin = False

      if ((robotChoice == "Rock" and choice == "3")
          or (robotChoice == "Paper" and choice == "1")
          or (robotChoice == "Scissors" and choice == "2")):
        robotWin = True
      elif ((robotChoice == "Rock" and choice == "2")
            or (robotChoice == "Paper" and choice == "3")
            or (robotChoice == "Scissors" and choice == "1")):
        humanWin = True

      robotFighter.respond(robotWin, humanWin)

      gameRounds += 1


if __name__ == "__main__":
  main()

