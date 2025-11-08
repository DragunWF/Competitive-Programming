# https://www.codewars.com/kata/56abc5e63c91630882000057/train/python

from typing import Union


def next_numb(val: int) -> Union[int, str]:
    for n in range(val + 1, 9999999999):
        str_num = str(n)
        if n % 2 != 0 and n % 3 == 0 and len(set(str_num)) == len(str_num):
            return n
    return "There is no possible number that fulfills those requirements"


def test() -> None:
    # Expected: 15
    print(next_numb(12))
    # Expected: 105
    print(next_numb(99))
    # Expected: "There is no possible number that fulfills those requirements"
    print(next_numb(9999999999))


if __name__ == "__main__":
    test()
