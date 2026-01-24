# https://www.codewars.com/kata/5aec1ed7de4c7f3517000079/train/python

def first_n_smallest(arr: list[int], n: int) -> list[int]:
    if not n:
        return []
    sorted_arr = sorted(arr)[:n]
    smallest_elements_in_order = []
    for number in arr:
        if number in sorted_arr:
            smallest_elements_in_order.append(number)
            sorted_arr.pop(sorted_arr.index(number))
        if len(smallest_elements_in_order) >= n:
            break
    return smallest_elements_in_order


def test() -> None:
    # Expected: [1, 2, 3]
    print(first_n_smallest([1, 2, 3, 4, 5], 3))
    # Expected: [3, 2, 1]
    print(first_n_smallest([5, 4, 3, 2, 1], 3))
    # Expected: []
    print(first_n_smallest([1, 2, 3, 4, 5], 0))
    # Expected: [1, -4, 0]
    print(first_n_smallest([1, 2, 3, -4, 0], 3))
    # Expected: [-3, -5, -2, -10, -1, -3, -4, -8, -7, -2, -2]
    print(first_n_smallest([10, -3, 5, 9, 0, 5, -5, 3, 0, -2, -10, -1, -1,
          7, -3, -4, 5, 10, -1, 10, 10, -8, -7, 6, 3, -2, -2, 1, 0, 1, 5], 11))


if __name__ == "__main__":
    test()
