# https://www.codewars.com/kata/59b0492f7d3c9d7d4a0000bd/train/python

def is_madhav_array(arr: list[int]) -> bool:
    if len(arr) <= 1:
        return False

    current_len, current_max_len = 0, 2
    current_sum = 0
    for i in range(1, len(arr)):
        current_sum += arr[i]
        current_len += 1
        if current_len == current_max_len:
            if current_sum != arr[0]:
                return False
            current_sum = 0
            current_max_len += 1
            current_len = 0
        elif i + 1 == len(arr):
            return False
    return True


def test() -> None:
    print(is_madhav_array([2, 1, 1, 4, -1, -1]))


test()
