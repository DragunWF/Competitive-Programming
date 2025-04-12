# https://www.codewars.com/kata/5832db03d5bafb7d96000107/train/python

def lottery(s: str) -> str:
    digits = []
    for char in s:
        if char.isdigit() and not char in digits:
            digits.append(char)
    return "".join(digits) if digits else "One more run!"
