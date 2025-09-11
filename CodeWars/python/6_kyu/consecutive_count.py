# https://www.codewars.com/kata/59c3e819d751df54e9000098/train/python

from typing import Union


def get_consective_items(items: Union[str, int], key: Union[str, int]) -> int:
    max_consecutive_count = 0
    current_consecutive_count = 0
    standardized_item = str(items)
    standardized_key = str(key)
    for i, char in enumerate(standardized_item):
        if char == standardized_key:
            if current_consecutive_count == 0:
                current_consecutive_count = 1
            elif standardized_item[i - 1] == standardized_key:
                current_consecutive_count += 1
        else:
            if current_consecutive_count > max_consecutive_count:
                max_consecutive_count = current_consecutive_count
            current_consecutive_count = 0
    if current_consecutive_count > max_consecutive_count:
        max_consecutive_count = current_consecutive_count
    return max_consecutive_count


def test() -> None:
    print(get_consective_items(90000, 0))  # 4
    print(get_consective_items("abcdaaadse", "a"))  # 3
    print(get_consective_items("abcdaaadse", "z"))  # 0


if __name__ == "__main__":
    test()
