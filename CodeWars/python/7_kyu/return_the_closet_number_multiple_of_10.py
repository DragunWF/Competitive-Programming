# https://www.codewars.com/kata/58249d08b81f70a2fc0001a4

from typing import Union


def closest_multiple_10(n: Union[int, float]) -> Union[int, float]:
    first_number = n % 10
    if first_number >= 5:
        return round(n + (10 - first_number))
    return round(n - first_number)


def test() -> None:
    print(closest_multiple_10(17))
    print(closest_multiple_10(23))


if __name__ == "__main__":
    test()
