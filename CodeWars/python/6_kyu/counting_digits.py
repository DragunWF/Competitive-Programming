# https://www.codewars.com/kata/5d41d87bb29859002690d4fd

from collections import Counter


def count_digits(num: int, rounds: int) -> list[int]:
    str_num = str(num)
    digit_counter = Counter(str_num)
    found = set()
    output = []
    for digit in str_num:
        if not digit in found:
            count = digit_counter[digit]
            found.add(digit)
            output.append(f"{count}{digit}")
    if rounds - 1 > 0:
        return count_digits(int("".join(output)), rounds - 1)
    return [int(item) for item in output]


def test() -> None:
    print(count_digits(141, 1))  # [21, 14]
    print(count_digits(1, 2))  # [21]
    print(count_digits(13, 2))  # [31, 13]
    print(count_digits(13, 8))  # [14, 12, 31, 13]


if __name__ == "__main__":
    test()
