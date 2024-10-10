# https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

def roman_fractions(n, fraction=None):
    if (n < 0 or n > 5000) or (fraction is not None and (fraction < 0 or fraction > 12)) or (n == 0 and fraction == 12):
        return "NaR"
    if n == 0 and (fraction is None or fraction == 0):
        return "N"
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
    fraction_values = ((
        ".", ":", ":.", "::",
        ":.:", "S", "S.", "S:",
        "S:.", "S::", "S:.:", "I"
    ))
    output = ""
    for symbol in values:
        symbol_count = n // values[symbol]
        if symbol_count >= 1:
            n -= symbol_count * values[symbol]
            output += symbol * symbol_count
    return f"{output}{fraction_values[fraction - 1]}" if fraction else output
