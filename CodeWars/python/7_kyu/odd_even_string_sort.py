# https://www.codewars.com/kata/580755730b5a77650500010c/train/python

def sort_my_string(s: str) -> str:
    even = ""
    odd = ""
    for i, char in enumerate(s):
        if i % 2 == 0:
            even += char
        else:
            odd += char
    return f"{even} {odd}"
