# https://www.codewars.com/kata/586c7cd3b98de02ef60001ab/train/python

from math import factorial
from collections import Counter


def uniq_count(s: str) -> int:
    if not s:
        return 1
    n = len(s)
    counter = Counter(s.upper())
    denominator = None
    for char in counter:
        if denominator is None:
            denominator = factorial(counter[char])
        else:
            denominator *= factorial(counter[char])
    return factorial(n) // denominator


def test() -> None:
    print(uniq_count("ABC"))  # 6
    print(uniq_count("ABBb"))  # 4
    print(uniq_count("BANANA"))  # 60


if __name__ == "__main__":
    test()
