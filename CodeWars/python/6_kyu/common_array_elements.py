# https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/python

from collections import Counter


def common(a: list, b: list, c: list) -> int:
    common_elements = set(a) & set(b) & set(c)
    counter_a = Counter(a)
    counter_b = Counter(b)
    counter_c = Counter(c)

    total = 0
    for element in common_elements:
        min_count = min([counter_a[element], counter_b[element], counter_c[element]])
        total += min_count * element

    return total


def test() -> None:
    # = 5 because 2 & 3 are common in all 3 arrays
    print(common([1, 2, 3], [5, 3, 2], [7, 3, 2]))  #
    # = 7 because 2, 2 & 3 are common in the 3 arrays
    print(common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]))


if __name__ == "__main__":
    test()
