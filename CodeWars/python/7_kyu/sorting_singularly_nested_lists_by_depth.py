# https://www.codewars.com/kata/67a61fa0ed1d3932f2c39b66/train/python

from typing import Union


def sort_by_depth(arr: list) -> list:
    sorted_data_set = arr.copy()

    def count_depth(element: list, count=1) -> Union[int, None]:
        if len(element) == 1:
            return count_depth(element[0], count + 1)
        return count

    sorted_data_set.sort(key=lambda element: count_depth(element))
    return sorted_data_set


def test() -> None:
    # Expected: [ [], [], [[]], [[[]]], [[[[[]]]]] ]
    print(sort_by_depth([[[[[[]]]]], [[]], [], [[[]]], []]))


if __name__ == "__main__":
    test()
