# https://www.codewars.com/kata/55e9529cbdc3b29d8c000016/train/python

from string import ascii_letters


def char_to_ascii(s: str) -> list[dict] | None:
    if not s:
        return None
    output = {}
    for char in set(char for char in s if char in ascii_letters):
        output[char] = ord(char)
    return output
