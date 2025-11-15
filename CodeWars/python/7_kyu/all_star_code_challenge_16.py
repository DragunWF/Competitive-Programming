# https://www.codewars.com/kata/586566b773bd9cbe2b000013

from collections import Counter


def no_repeat(string: str):
    counter = Counter(string)
    for char in string:
        if counter[char] == 1:
            return char
