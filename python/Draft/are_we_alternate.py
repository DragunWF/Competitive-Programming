# https://www.codewars.com/kata/59325dc15dbb44b2440000af/train/python

def is_alt(s):
    VOWELS = "aeiouAEIOU"
    alternate = False
    for char in s:
        if char in VOWELS:
            if not alternate:
                alternate = False
            alternate = True
    return True
