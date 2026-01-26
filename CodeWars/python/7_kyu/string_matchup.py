# https://www.codewars.com/kata/59ca8e8e1a68b7de740001f4/train/python

from collections import Counter


def solve(a: list[str], b: list[str]) -> list[int]:
    counter = Counter(a)
    output = []
    for element in b:
        output.append(counter[element] if element in counter else 0)
    return output


def test() -> None:
    print(solve(['abc', 'abc', 'xyz', 'cde', 'uvw'],
                ['abc', 'cde', 'uap']))


if __name__ == "__main__":
    test()
