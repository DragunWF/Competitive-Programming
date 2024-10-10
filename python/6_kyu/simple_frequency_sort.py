# https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/train/python

from collections import Counter


def solve(arr: list[int]) -> list[int]:
    counter = Counter(arr)
    order = [key for key in counter]
    for i in range(len(order) - 1):
        for j in range(len(order) - 1):
            if (counter[order[j]] == counter[order[j + 1]] and order[j] > order[j + 1]) or counter[order[j]] < counter[order[j + 1]]:
                order[j + 1], order[j] = order[j], order[j + 1]

    output = []
    for key in order:
        for i in range(counter[key]):
            output.append(key)
    return output


def test():
    print(solve([2, 3, 5, 3, 7, 9, 5, 3, 7]))  # [3,3,3,5,5,7,7,2,9]
    print(solve([5, 9, 6, 9, 6, 5, 9, 9, 4, 4]))  # [9,9,9,9,4,4,5,5,6,6]


if __name__ == '__main__':
    test()
