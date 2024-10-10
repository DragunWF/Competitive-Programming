# https://www.codewars.com/kata/586538146b56991861000293/train/python

from preloaded import NATO  # NATO['A'] == 'Alfa', etc


def to_nato(words: str) -> str:
    output = []
    for char in words.upper():
        if char == " ":
            continue
        output.append(NATO[char] if char in NATO else char)
    return " ".join(output)
