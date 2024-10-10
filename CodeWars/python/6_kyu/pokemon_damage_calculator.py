# https://www.codewars.com/kata/536e9a7973130a06eb000e9f/train/python

def calculate_damage(your_type, opponent_type, attack, defense):
    effectiveness = 1
    elements = {
        "fire": {"grass": 2, "water": 0.5},
        "water": {"fire": 2, "grass": 0.5, "electric": 0.5},
        "grass": {"fire": 0.5, "water": 2},
        "electric": {"water": 2}
    }
    if opponent_type == your_type:
        effectiveness = 0.5
    elif opponent_type in elements[your_type]:
        effectiveness = elements[your_type][opponent_type]
    return 50 * (attack / defense) * effectiveness
