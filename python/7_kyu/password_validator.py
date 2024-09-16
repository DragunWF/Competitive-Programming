# https://www.codewars.com/kata/56a921fa8c5167d8e7000053/train/python

from string import digits
from string import ascii_uppercase as uppercase
from string import ascii_lowercase as lowercase


def password(s: str) -> bool:
    if len(s) < 8:
        return False
    has_digits, has_lower, has_upper = False, False, False
    for char in s:
        if char in digits:
            has_digits = True
        elif char in lowercase:
            has_lower = True
        elif char in uppercase:
            has_upper = True
    return has_digits and has_lower and has_upper
