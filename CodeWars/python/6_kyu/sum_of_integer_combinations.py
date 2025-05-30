# https://www.codewars.com/kata/59f3178e3640cef6d90000d5/train/python

from itertools import combinations_with_replacement


def find(arr: list, n: int) -> int:
    count = 0
    for i in range(1, len(arr) + 1):
        possibilities = list(combinations_with_replacement(arr, i))
        for possibility in possibilities:
            if sum(possibility) == n:
                count += 1
    return count


def test() -> None:
    print(find([3, 6, 9, 12], 12))  # 5


if __name__ == "__main__":
    test()
