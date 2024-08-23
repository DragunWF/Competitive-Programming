# https://www.codewars.com/kata/57a37f3cbb99449513000cd8/train/python


def get_number_from_string(s: str):
    return int("".join([char for char in s if char.isdigit()]))
