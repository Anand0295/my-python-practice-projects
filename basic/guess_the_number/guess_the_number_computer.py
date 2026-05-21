# The guessing game where computer generates a random number using 'random.randint' method by importing 'random' module, which the user has to guess

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
# random_number = 7

Guess: 8 → 8 > 7 → Too high
Guess: 5 → 5 < 7 → Too low
Guess: 7 → correct → win

# guess != random_number → loop continues
# guess == random_number → loop stops
"""
