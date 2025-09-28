# https://www.codewars.com/kata/57882daf90b2f375280000ad/train/python

from typing import Union


def sumsquares(lst: list) -> int:
    total = 0

    def recursive_summation(items: list[Union[int, list]]) -> None:
        nonlocal total
        for item in items:
            if type(item) is list:
                recursive_summation(item)
            else:
                total += item ** 2

    recursive_summation(lst)
    return total


def test() -> None:
    print(sumsquares([10, [[10], 10], [10]]))


if __name__ == "__main__":
    test()
