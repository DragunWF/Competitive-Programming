# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
from rich import print


def rgb(r: int, g: int, b: int) -> str:
    return f"{convert(r)}{convert(g)}{convert(b)}"


def convert(num) -> str:
    hexadecimal, base = (*range(10), "A", "B", "C", "D", "E", "F"), 16
    num = 255 if num > 255 else num
    if num <= (base - 1):
        return f"0{hexadecimal[num if num >= 0 else 0]}"
    return f"{hexadecimal[num // base]}{hexadecimal[num % base]}"


test_cases = (
    (0, 0, 0),  # 000000
    (1, 2, 3),  # 010203
    (255, 255, 255),  # FFFFFF
    (254, 253, 252),  # FEFDFC
    (-20, 275, 125)  # 00FF7D
)
for case in test_cases:
    print(rgb(case[0], case[1], case[2]))
