# https://www.codewars.com/kata/554e52e7232cdd05650000a0/train/python

import math


def lowest_product(num: str) -> int | str:
    n = len(num)
    if n < 4:
        return "Number is too small"

    arr = list(map(int, num))
    lowest_product = math.inf
    for i in range(n - 3):
        current_product = arr[i]
        for j in range(i + 1, i + 4):
            current_product *= arr[j]
        if current_product < lowest_product:
            lowest_product = current_product
    return lowest_product


def test() -> None:
    print(lowest_product("123456789"))


if __name__ == "__main__":
    test()
