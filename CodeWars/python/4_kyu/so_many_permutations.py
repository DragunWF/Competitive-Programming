# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

import itertools


def permutations(s: str) -> list[str]:
    return list(set(["".join(permutation) for permutation in itertools.permutations(s)]))


def test():
    print(permutations("Hack"))


if __name__ == "__main__":
    test()
