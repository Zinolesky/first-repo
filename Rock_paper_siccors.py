# Rock Paper Scissors game

import random
from tkinter import FALSE

options = ("Rock", "Paper", "Scissors")
player_score = 0
computer_score = 0
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:

        player = input("Rock, Paper, Sciccors!: ").capitalize()
        print(f"Player: {player}")
        print(f"Computer {computer}")

        if player == computer:
            print("Draw!")
            player_score += 0
            computer_score += 0
        elif player == "Rock" and computer == "Scissors":
            print("You win!")
            player_score += 1
            computer_score += 0
        elif player == "Paper" and computer == "Rock":
            print("You win!")
            player_score += 1
            computer_score += 0
        elif player == "Scissors" and computer == "Paper":
            print("You win!")
            player_score += 1
            computer_score += 0
        else:
            print("You lose!")
            player_score += 0
            computer_score += 1
    # Shortened
    if not input("Play again? (Y/N): ").capitalize() == "Y":
        running = False

print()
print("----- SCORE -----")

print(f"Player: {player_score}")
print(f"Computer: {computer_score}")
