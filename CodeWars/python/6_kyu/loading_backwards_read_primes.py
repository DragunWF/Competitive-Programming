# https://www.codewars.com/kata/5539fecef69c483c5a000015/train/python

from math import sqrt


def backwards_prime(start: int, stop: int) -> int:
    prime_numbers = []
    for num in range(start, stop + 1):
        if num <= 11:
            continue
        reversed_num = int(str(num)[::-1])
        if num != reversed_num and is_prime(num) and is_prime(reversed_num):
            prime_numbers.append(num)
    return prime_numbers


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def test() -> None:
    # [13, 17, 31, 37, 71, 73, 79, 97]
    print(backwards_prime(1, 97))


if __name__ == "__main__":
    test()
