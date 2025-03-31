# https://www.codewars.com/kata/56dc695b2a4504b95000004e/train/python

from string import ascii_uppercase


def caeser(message: str, key: int) -> str:
    output = ""
    for char in message.upper():
        if not char in ascii_uppercase:
            output += char
            continue
        ascii_pos = ascii_uppercase.index(char)
        output += ascii_uppercase[(ascii_pos + key) % len(ascii_uppercase)]
    return output
