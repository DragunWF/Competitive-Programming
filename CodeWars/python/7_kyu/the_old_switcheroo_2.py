# https://www.codewars.com/kata/55d6a0e4ededb894be000005/train/python


def encode(s: str) -> str:
    output = ""
    for char in s.upper():
        output += str(ord(char) - 64) if char.isalpha() else char
    return output
