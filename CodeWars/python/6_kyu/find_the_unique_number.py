# https://www.codewars.com/kata/55f81f9aa51f9b72a200002f/train/python

from collections import Counter


def find_unique(numbers: list[int]) -> int:
    counter = Counter(numbers)
    for key in counter:
        if counter[key] == 1:
            return key


def test() -> None:
    # Expected: 6
    print(find_unique([1, 8, 4, 4, 6, 1, 8]))


if __name__ == "__main__":
    test()
