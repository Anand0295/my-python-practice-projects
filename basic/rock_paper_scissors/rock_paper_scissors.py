# A simple Rock-Paper-Scissors game where the user plays against the computer using random choices to determine the winner.

import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors. ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        print("its a tie")

    elif is_win(user, computer):
        print("you Won!!")

    elif is_win(computer, user):
        print("you lost.")

    # s>p, p>r, r>s


def is_win(player, opponent):
    # return true if player wins
    # s>p, p>r, r>s
    if (
        (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
        or (player == "r" and opponent == "s")
    ):
        return True


play()

"""
What's your choice? 'r' for rock, 'p' for paper, 's' for scissors. r
you lost.

What's your choice? 'r' for rock, 'p' for paper, 's' for scissors. s
you Won!!

What's your choice? 'r' for rock, 'p' for paper, 's' for scissors. p
you Won!!
"""
