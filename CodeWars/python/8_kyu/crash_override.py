# https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/train/python

FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst'}


def alias_gen(f_name: str, l_name: str) -> str:
    if not f_name[0].isalpha() or not l_name[0].isalpha():
        return "Your name must start with a letter from A - Z."
    return f"{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}"
