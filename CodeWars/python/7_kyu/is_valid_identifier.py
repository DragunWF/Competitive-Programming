# https://www.codewars.com/kata/563a8656d52a79f06c00001f/train/python

from string import ascii_letters, digits


def is_valid(identifier: str) -> bool:
    if not identifier:
        return False

    valid = f"{ascii_letters}_$"
    first_char = identifier[0]
    if not first_char in valid:
        return False
    valid += digits
    return all(char in valid for char in identifier)
