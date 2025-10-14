# https://www.codewars.com/kata/55c606e6babfc5b2c500007c/train/python

def filter_numbers(string: str) -> str:
    return "".join(x for x in string if not x.isdigit())
