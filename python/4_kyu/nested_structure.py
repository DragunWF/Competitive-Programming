# https://www.codewars.com/kata/520446778469526ec0000001
from rich import print


def same_structure_as(original, other) -> bool:
    if type(original) != type(other):
        return False
    return [count_nested(x) for x in original] == [count_nested(x) for x in other]


def count_nested(item):
    if type(item) == list:
        return [count_nested(x) for x in item]
    return True


def test():
    test_cases = [
        [[1, [1, 1]], [2, [2, 2]]],
        [[1, [1, 1]], [[2, 2], 2]]
    ]
    for case in test_cases:
        print(same_structure_as(case[0], case[1]))


if __name__ == "__main__":
    test()
