# https://www.codewars.com/kata/6a1f03fac18f58f98ad9d21a/train/python

from math import log2
from string import punctuation


def entropy(password: str) -> float:
    r = 0
    lowercase_present = False
    uppercase_present = False
    digits_present = False
    special_present = False
    for char in password:
        if not lowercase_present and char.islower():
            lowercase_present = True
            r += 26
        elif not uppercase_present and char.isupper():
            uppercase_present = True
            r += 26
        elif not digits_present and char.isdigit():
            digits_present = True
            r += 10
        elif not special_present and char in punctuation:
            special_present = True
            r += 32
    return len(password) * log2(r)
