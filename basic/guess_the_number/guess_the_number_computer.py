import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess > random_number:
            print("Sorry, guess again. Too high.")
        elif guess < random_number:
            print("Sorry, guess again. Too low.")

    print(f"Yay, congrats. You have guessed the number {x} correctly!!")


guess(10)

"""
Guess the number between 1 and 10: 8
Sorry, guess again. Too high.
Guess the number between 1 and 10: 5
Yay, congrats. You have guessed the number 10 correctly!!
"""
