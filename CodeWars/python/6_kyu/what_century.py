# https://www.codewars.com/kata/52fb87703c1351ebd200081f

import math


def what_century(year):
    century = str(math.ceil(int(year) / 100))
    if 10 <= int(century) <= 20:
        return f"{century}th"
    match century[-1]:
        case "1":
            century += "st"
        case "2":
            century += "nd"
        case "3":
            century += "rd"
        case _:
            century += "th"
    return century


def test():
    # Not part of the solution
    test_cases = ("1999", "2011", "2154", "2259", "1124", "2000", "1234")
    for case in test_cases:
        print(f'"{case}" --> "{what_century(case)}"')


if __name__ == "__main__":
    test()
