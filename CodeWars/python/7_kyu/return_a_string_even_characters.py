# https://www.codewars.com/kata/566044325f8fddc1c000002c/train/python

def even_chars(s: str) -> str:
    if len(s) <= 1 or len(s) > 100:
        return "invalid string"
    return [char for i, char in enumerate(s) if (i + 1) % 2 == 0]
