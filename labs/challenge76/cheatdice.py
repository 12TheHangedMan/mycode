#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

class Cheat_mulligan(Player): #re-roll if sum less than 9. bad sport?
    def cheat(self):
        sum = 0
        for die in self.get_dice():
            sum += die
        while(sum < 9):
            self.__init__()
            self.roll()
            for die in get_dice(self):
                sum+=die

class Cheat_additional_die(Player): #roll one additional die
    def cheat(self):
        additionaldie = randint(1,6)
        self.dice.append(additionaldie)

class Cheat_Weighted_Dice(Player): #weighted dice, 1th die can not rolling a below 3
    def cheat(self):
        weighteddie = randint(3,6)
        self.dice[0] = weighteddie

class Cheat_SABOTAGE(Player): #replaced the other player's dice with die that won't roll about 3
    def cheat(self, player2):
        for i in range(3):
            player2.dice[i] = randint(1,3)

