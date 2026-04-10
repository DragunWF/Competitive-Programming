# https://www.codewars.com/kata/58334362c5637ad0bb0001c2

import re


def valid_romans(arr: list[str]) -> list[str]:
    output = []
    for numeral in arr:
        if is_valid_roman(numeral) and (1 <= roman_value(numeral) < 5000):
            output.append(numeral)
    return output


def is_valid_roman(numeral: str) -> bool:
    return bool(re.search(r"^M{0,10}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", numeral))


def roman_value(numeral: str) -> int:
    values = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    output = 0
    is_skip = False
    for i in range(len(numeral)):
        if is_skip:
            is_skip = False
            continue
        symbol = numeral[i]
        next_symbol = numeral[i + 1] if i + 1 != len(numeral) else None
        if f"{symbol}{next_symbol}" in values:
            output += values[f"{symbol}{next_symbol}"]
            is_skip = True
        else:
            output += values[symbol]
    return output
