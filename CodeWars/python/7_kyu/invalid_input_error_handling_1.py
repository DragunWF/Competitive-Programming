# https://www.codewars.com/kata/55e6125ad777b540d9000042/train/python

from string import ascii_lowercase


def get_count(word=None):
    VOWELS = "aeiou"
    output = {"vowels": 0, "consonants": 0}
    if type(word) != str:
        return output

    for char in word.lower():
        if char in VOWELS:
            output["vowels"] += 1
        elif char in ascii_lowercase:
            output["consonants"] += 1

    return output
