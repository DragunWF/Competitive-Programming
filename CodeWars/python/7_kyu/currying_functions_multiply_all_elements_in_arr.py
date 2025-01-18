# https://www.codewars.com/kata/586909e4c66d18dd1800009b/train/python

from collections.abc import Callable


def multiply_all(arr: list[int]) -> Callable:
    def helper(multiplier: int) -> list[int]:
        output = []
        for num in arr:
            output.append(num * multiplier)
        return output
    return helper
