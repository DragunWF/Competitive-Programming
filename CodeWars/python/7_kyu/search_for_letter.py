# https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python

from string import ascii_lowercase as lowercase


def change(s: str) -> str:
    alphabets = [*("0" * 26)]
    for char in s.lower():
        if char in lowercase:
            alphabets[lowercase.index(char)] = "1"
    return "".join(alphabets)
