# https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numeral_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = None
        subtract_combos = (("I", "X", "C"), ("V", "X", "L", "C", "D", "M"))
        for char in s:
            if prev == "I" and char in ("V", "X"):
                total -= 2
            elif prev == "X" and char in ("L", "C"):
                total -= 20
            elif prev == "C" and char in ("D", "M"):
                total -= 200
            total += roman_numeral_values[char]
            prev = char
        return total