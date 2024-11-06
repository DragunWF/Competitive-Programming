# https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, val: int) -> str:
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
        current_val = val
        output = ""
        for symbol in values:
            symbol_count = current_val // values[symbol]
            if symbol_count >= 1:
                current_val -= symbol_count * values[symbol]
                output += symbol * symbol_count
        return output