# https://www.codewars.com/kata/55486cb94c9d3251560000ff/train/python

from math import gcd


def calculate_ratio(w: int, h: int) -> str:
    greatest_common_divisor = gcd(w, h)
    height_ratio = h // greatest_common_divisor
    width_ratio = w // greatest_common_divisor
    if not height_ratio or not width_ratio:
        raise Exception("Ratio cannot have a zero!")
    return f"{width_ratio}:{height_ratio}"


def test() -> None:
    print(calculate_ratio(1024, 768))


if __name__ == "__main__":
    test()
