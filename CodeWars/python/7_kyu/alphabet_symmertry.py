# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python

from string import ascii_lowercase


def solve(strings: list[str]) -> list[int]:
    output = []
    for string in strings:
        count = 0
        for i, char in enumerate(string.lower()):
            if i >= len(ascii_lowercase):
                break
            if ascii_lowercase[i] == char:
                count += 1
        output.append(count)
    return output


def test() -> None:
    print(solve(["abode", "ABc", "xyzD"]))  # [4, 3, 1]


if __name__ == "__main__":
    test()
