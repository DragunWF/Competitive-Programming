# https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/python

def capitalize(s: str, ind: list[int]) -> str:
    output = ""
    for i in range(len(s)):
        output += s[i].upper() if i in ind else s[i]
    return output
