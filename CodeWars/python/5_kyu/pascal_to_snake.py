# https://www.codewars.com/kata/529b418d533b76924600085d/train/python

from string import digits


def to_underscore(string: str):
    output = ""
    for i, item in enumerate(str(string)):
        if item == item.upper() and not item in digits and i != 0:
            output += "_"
        output += item.lower()
    return output
