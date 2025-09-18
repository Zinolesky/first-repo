import random

words = ("APPLE", "ORANGE", "BANANA", "COCONUT", "PINEAPPLE")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    no_of_plays = 0
    no_of_wins = 0
    no_of_loss = 0

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue

        if guess in guessed_letters:
            print(f"{guess} has already been guessed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You win!")
            no_of_plays += 1
            no_of_wins += 1

            answer = random.choice(words)
            hint = ["_"] * len(answer)
            wrong_guesses = 0
            guessed_letters = set()

            if input("Play again? (Y/N): ").upper() != "Y":
                is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lose")
            no_of_plays += 1
            no_of_loss += 1

            answer = random.choice(words)
            hint = ["_"] * len(answer)
            wrong_guesses = 0
            guessed_letters = set()

            if input("Play again? (Y/N): ").upper() != "Y":
                is_running = False

            print()
            print(f"Number of games: {no_of_plays:>15}")
            print(f"Number of wins {no_of_wins:>16}")
            print(f"Number of losses {no_of_loss:>14}")


if __name__ == "__main__":
    main()