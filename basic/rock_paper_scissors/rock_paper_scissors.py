import random

def play():
    user = input('What's your choice? 'r' for rock, 'p' for paper, 's' for scissors. )
    computer=random.choice(['r','p','s'])

    if user==computer:
        print('its a tie')

    #s>p, p>r, r>s

    def is_win(player, opponent):
        if (player =='s' and opponent=='p') or (player=='p' and opponent=='r') or (player=='r' or opponent=='s'):
            return True