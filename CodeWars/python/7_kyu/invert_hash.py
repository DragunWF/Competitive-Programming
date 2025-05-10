# https://www.codewars.com/kata/5b5604e26dc79e6832000101/train/python

def invert_hash(dictionary: dict) -> dict:
    output = {}
    for key, value in dictionary.items():
        output[value] = key
    return output
