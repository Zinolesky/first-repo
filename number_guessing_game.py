# Python Guessing Game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"Choose a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Number out of range! Try again!")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print("Correct!")
            print(f"The answer is {answer}")
            is_running = False

    else:
        print("Invalid input!")
        print(f"Choose a number between {lowest_num} and {highest_num}")

print(f"You found the answer in {guesses} guesses.")
