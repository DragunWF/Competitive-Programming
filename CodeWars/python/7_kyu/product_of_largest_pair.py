# https://www.codewars.com/kata/5784c89be5553370e000061b

import heapq


def max_product(a: list[int]) -> int:
    largest = heapq.nlargest(2, a)
    return largest[0] * largest[1]


def test() -> None:
    # Expected: 20
    print(max_product([2, 1, 5, 0, 4, 3]))


if __name__ == "__main__":
    test()
