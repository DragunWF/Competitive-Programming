# https://www.codewars.com/kata/59c6fa6972851e8959000067/train/python

from collections import Counter


def is_zero_balanced(arr: list[str]) -> bool:
    if not arr:
        return False
    counter = Counter(arr)
    for num in counter:
        if counter[num] != counter[invert_num(num)]:
            return False
    return True


def invert_num(num: int) -> int:
    return -num if num > 0 else abs(num)


def test() -> None:
    print(is_zero_balanced([-3]))  # False


if __name__ == "__main__":
    test()
