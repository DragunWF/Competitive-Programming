# https://www.codewars.com/kata/51b66044bce5799a7f000003

class RomanNumerals:
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

    @staticmethod
    def to_roman(val: int) -> str:
        current_val = val
        values = RomanNumerals.values
        output = ""
        for symbol in values:
            symbol_count = current_val // values[symbol]
            if symbol_count >= 1:
                current_val -= symbol_count * values[symbol]
                output += symbol * symbol_count
        return output

    @staticmethod
    def from_roman(roman_num: str) -> int:
        output = 0
        values = RomanNumerals.values
        is_skip = False
        for i in range(len(roman_num)):
            if is_skip:
                is_skip = False
                continue
            symbol = roman_num[i]
            next_symbol = roman_num[i + 1] if i + 1 != len(roman_num) else None
            if f"{symbol}{next_symbol}" in values:
                output += values[f"{symbol}{next_symbol}"]
                is_skip = True
            else:
                output += values[symbol]
        return output


def test():
    print(RomanNumerals.to_roman(1990))  # MCMXC
    print(RomanNumerals.to_roman(1666))  # MDCLXVI
    print(RomanNumerals.from_roman("MDCLXVI"))  # 1666
    print(RomanNumerals.from_roman("IV"))  # 4
    print(RomanNumerals.from_roman("LXXXVI"))  # 86


if __name__ == "__main__":
    test()
