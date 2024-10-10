# https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

def solution(n):
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
    output = ""
    for symbol in values:
        symbol_count = n // values[symbol]
        if symbol_count >= 1:
            n -= symbol_count * values[symbol]
            output += symbol * symbol_count
    return output
