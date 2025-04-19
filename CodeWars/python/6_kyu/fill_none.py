# https://www.codewars.com/kata/5edaa69f5fcd510020199489/train/python

def fill(arr: list, method: int = 0):
    if not arr or len(arr) == 1:
        return arr

    if method == 0:
        fill_nearest(arr, [*arr])
    elif method == 1:
        fill_left(arr)
    else:
        fill_right(arr)
    return arr


def fill_nearest(arr: list, original_arr: list) -> None:
    for i in range(len(arr)):
        if arr[i] is None:
            arr[i] = get_nearest_min_int(original_arr, i)


def get_nearest_min_int(arr: list, i: int) -> int:
    left_num, right_num = None, None
    left_distance, right_distance = 0, 0
    for j in range(i - 1, -1, -1):
        left_distance += 1
        if not arr[j] is None:
            left_num = arr[j]
            break
    for j in range(i + 1, len(arr)):
        right_distance += 1
        if not arr[j] is None:
            right_num = arr[j]
            break

    if right_num is None or (left_num and left_distance < right_distance):
        return left_num
    if left_num is None or (right_num and right_distance < left_distance):
        return right_num
    return min(left_num, right_num)


def fill_left(arr: list) -> None:
    for i in range(1, len(arr)):
        if arr[i] is None:
            arr[i] = arr[i - 1]


def fill_right(arr: list) -> None:
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] is None:
            arr[i] = arr[i + 1]


def test() -> None:
    arr = [None, 1, None, None, None, 2, None]
    print(fill([*arr], -1))  # [1, 1, 2, 2, 2, 2, None]
    print(fill([*arr], 1))  # [None, 1, 1, 1, 1, 2, 2]
    print(fill([*arr], 0))  # [1, 1, 1, 1, 2, 2, 2]

    # [4, 5, 5, 2, 2, 2, 2, 2]
    print(fill([4, 5, None, None, None, 2, None, 2], 0))


if __name__ == "__main__":
    test()
