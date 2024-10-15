# https://www.codewars.com/kata/65128732b5aff40032a3d8f0/train/python

def neutralise(s1, s2):
    return "".join(char1 if char1 == char2 else "0" for char1, char2 in zip(s1, s2))
