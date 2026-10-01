# PROJECT 1: SNAKE, WATER, GUN GAME
"""
We all have played snake, water or gun game in our childhood. If you haven't, google the rules of this game and write a python program capable of playing this game with the user.
"""
# Rules to play snake, water or gun:-
'''
The Snake, Water, and Gun game follows a simple rule set. Each player chooses one of the three options (Snake, Water, or Gun) simultaneously. The winner is determined by the following matchups: Snake beats Water, Water beats Gun, and Gun beats Snake. If both players choose the same option, it's a tie. 
Here's a breakdown of the winning matchups: 
Snake vs. Water: The snake drinks the water, so the snake wins.
Water vs. Gun: The gun gets drowned in the water, so water wins.
Gun vs. Snake: The gun kills the snake, so the gun wins.
Same choice: If both players choose the same option, it's a draw.
'''

# 1 = for snake, -1 = for water, 0 = for gun

import random

# computer = -1
computer = random.choice([1, -1, 0])
# take user input
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = { 1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you ==1):
        print("You win!")
    elif(computer ==-1 and you ==0):
        print("You Lose!")
    elif (computer ==1 and you ==-1):
        print("You lose!")
    elif(computer ==1 and you ==0):
        print("You Win!")
    elif (computer ==0 and you ==-1):
        print("You Win!")
    elif(computer ==0 and you ==1):
        print("You Lose!")
    else:
        print("Something went wrong!")