import random

def get_board():
    cards = []
    with open('../codenames_cards.txt', 'r') as f:
        for r in f.readlines():
            cards.append(r.lower().strip().replace(' ', '_'))
            
    sample = random.sample(cards, 18)
    return {
        'positive': sample[:9],
        'negative': sample[9:-1],
        'assassin': sample[-1]
    }