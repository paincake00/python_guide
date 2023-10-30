# <ROCK-SCISSORS-PAPER-GAME>

import random

choices = {'rock': 'scissors', 
           'paper': 'rock', 
           'scissors': 'paper'}


def results(computer, player):
    print("Copmuter: "+computer)
    print("You: "+player)

while True:
    computer = random.choice(list(choices.keys()))
    player = ""
    while player not in choices.keys():
        player = input("Rock, scissors or paper? Enter your choice!\n").lower()
    if computer == player:
        results(computer, player)
        print("TIE!")
    else:
        if choices[player] == computer:
            results(computer, player)
            print("You win! :)")
        else:
            results(computer, player)
            print("You lose :(")    

    command = ""
    while command not in {"y", "n"}:
        command = input("Do you want to repeat? (y/n)\n").lower()
    if (command == "n"):
        print("bye!")
        break    