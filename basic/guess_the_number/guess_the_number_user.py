# The guessing game where computer has to guess the number using 'random.randint' method by importing 'random' module the user has thought of

import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} too high (H) too low (L) or correct (C) ??: "
        ).lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay, The computer has guessed the number {guess} correctly!!")


computer_guess(1000)

# low = 1, high = 1000

# Guess: 265 → H → high = 264
# Guess: 256 → C → win

# low increases when L
# high decreases when H
# loop continues until C

"""
Is 265 too high (H) too low (L) or correct (C) ??: h
Is 256 too high (H) too low (L) or correct (C) ??: c
Yay, The computer has guessed the number 256 correctly!!
"""
