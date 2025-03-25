# https://www.codewars.com/kata/57a153e872292d7c030009d4/train/python

def simple_transposition(text: str) -> str:
    encrypted = ["", ""]
    for i, char in enumerate(text):
        encrypted[i % 2] += char
    return "".join(encrypted)
