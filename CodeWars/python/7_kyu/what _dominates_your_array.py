# https://www.codewars.com/kata/559e10e2e162b69f750000b4/train/python

from collections import Counter


def dominator(arr: list[int]) -> int:
    if not arr:
        return -1
    counter = Counter(arr)
    max_count = 0
    max_num = 0
    for num in counter.keys():
        if counter[num] > max_count:
            max_count = counter[num]
            max_num = num
    if max_count <= len(arr) // 2:
        return -1
    return max_num


def test() -> None:
    # 3
    print(dominator([3, 4, 3, 2, 3, 1, 3, 3]))
    # 1
    print(dominator([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    test()
