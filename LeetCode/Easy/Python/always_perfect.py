# https://www.codewars.com/kata/55f3facb78a9fd5b26000036/train/python

from math import isqrt


def check_root(s: str) -> str:
    numbers = s.split(",")
    product = None
    if len(numbers) != 4:
        return "incorrect input"
    for i, str_num in enumerate(numbers):
        try:
            current_num = int(str_num)
            if product is None:
                product = current_num
            else:
                product *= current_num
                if i != 0 and int(numbers[i - 1]) != current_num - 1:
                    return "not consecutive"
        except ValueError:
            return "incorrect input"
    product += 1
    return f"{product}, {isqrt(product)}"


def get_root_from_perfect_square(num: int) -> int:
    if num < 0:
        return -1
    root = isqrt(num)
    if root * root == num:
        return root
    return -1


def test() -> None:
    # Expected: 841, 29
    print(check_root('4,5,6,7'))


if __name__ == "__main__":
    test()
