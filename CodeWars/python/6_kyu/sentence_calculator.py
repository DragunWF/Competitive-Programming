# https://www.codewars.com/kata/5970fce80ed776b94000008b/train/python

from string import ascii_lowercase


def letters_to_numbers(s: str) -> int:
    score = 0
    for char in s:
        if char.isupper():
            score += (ascii_lowercase.index(char.lower()) + 1) * 2
        elif char.islower():
            score += ascii_lowercase.index(char) + 1
        elif char.isdigit():
            score += int(char)
    return score
