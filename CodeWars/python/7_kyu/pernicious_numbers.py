# https://www.codewars.com/kata/56e195d02bb22479e50016af/train/python

import math


def pernicious(n: int) -> list | str:
    pernicious_numbers = []
    for i in range(1, math.floor(n) + 1):
        binary_num = digit_sum_of_bin(i)
        if is_prime(binary_num):
            pernicious_numbers.append(i)
    return pernicious_numbers if pernicious_numbers else "No pernicious numbers"


def digit_sum_of_bin(n: int):
    return sum([int(digit) for digit in bin(n)[2:]])


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    output = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            output = False
            break
    return output


def test() -> None:
    print(pernicious(5))


if __name__ == "__main__":
    test()
