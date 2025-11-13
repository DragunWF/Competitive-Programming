# https://www.codewars.com/kata/56b18992240660a97c00000a/train/python

from itertools import permutations


def permutation_average(n: int) -> int:
    digit_permutations = list([int("".join(item))
                              for item in permutations(str(n))])
    return round(sum(digit_permutations) / len(digit_permutations))


def test() -> None:
    print(permutation_average(1256))  # 3889.


if __name__ == "__main__":
    test()
