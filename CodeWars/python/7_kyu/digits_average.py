# https://www.codewars.com/kata/5a32526ae1ce0ec0f10000b2/train/python

from math import ceil


def digits_average(x: int) -> int:
    current_digits = [int(n) for n in str(x)]
    averaged_digits = []
    while len(current_digits) > 1:
        for i in range(1, len(current_digits)):
            averaged_digits.append(
                ceil((current_digits[i - 1] + current_digits[i]) / 2)
            )
        current_digits = [*averaged_digits]
        averaged_digits.clear()
    return current_digits[0]


def test() -> None:
    print(digits_average(246))  # 4


if __name__ == "__main__":
    test()
