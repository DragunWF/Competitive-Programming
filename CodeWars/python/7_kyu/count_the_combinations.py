# https://www.codewars.com/kata/58e67378fd2d897b8a000110/train/python

from itertools import combinations


def num_combo(xs: list, n: int) -> int:
    size = len(xs) - 1
    all_combinations = list(combinations(xs, size))
    target_combinations_count = 0
    for combination in all_combinations:
        if sum(combination) == n:
            target_combinations_count += 1
    return target_combinations_count


def test() -> None:
    print(num_combo([2, 0, 0, 0, 1], 1))  # 1
    print(num_combo([2, 0, 0, 0, 1], 3))  # 3


if __name__ == "__main__":
    test()
