# https://www.codewars.com/kata/56fcfad9c7e1fa2472000034/train/python

from collections import Counter


def evil(n: int) -> str:
    digit_counter = Counter(bin(n)[2:])
    return f"It's {'Evil' if digit_counter['1'] % 2 == 0 else 'Odious'}!"


def test() -> None:
    print(evil(1))


if __name__ == "__main__":
    test()
