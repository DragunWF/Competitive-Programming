# https://www.codewars.com/kata/5612a42e746aa62de100001a/train/python

from math import log10


def db_scale(intensity: int) -> int:
    return round(log10(intensity / 10 ** -12) * 10)


def test() -> None:
    print(db_scale(10 ** -9))  # 30
    print(db_scale(10 ** -5))  # 70
    print(db_scale(2.48794569 * 10**173))  # 1854


if __name__ == "__main__":
    test()
