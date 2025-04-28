# https://www.codewars.com/kata/55de6173a8fbe814ee000061/train/python

from string import digits


def unused_digits(*numbers: list[int]) -> str:
    output = ""
    all_present_digits = "".join(str(num) for num in numbers)
    for digit in digits:
        if not digit in all_present_digits:
            output += (digit)
    return output
