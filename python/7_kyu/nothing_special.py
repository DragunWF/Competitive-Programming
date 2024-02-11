# https://www.codewars.com/kata/57029e77005264a3b9000eb5/train/python

from string import ascii_letters, digits


def nothing_special(st):
    if (type(st) != str):
        return "Not a string!"
    output = ""
    for char in st:
        if char in ascii_letters or char in digits or char.isspace():
            output += char
    return output
