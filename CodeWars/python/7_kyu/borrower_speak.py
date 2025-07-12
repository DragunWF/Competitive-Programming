# https://www.codewars.com/kata/57d2ba8095497e484e00002e/train/python

from string import ascii_lowercase


def borrow(s: str) -> str:
    return "".join(char for char in s.lower() if char in ascii_lowercase)
