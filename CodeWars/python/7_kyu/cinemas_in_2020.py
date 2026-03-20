# https://www.codewars.com/kata/68b0064510c5854a66e6323a/train/python

def maximum_seating(arr: list[int]) -> int:
    maximum_seats = 0
    for i, num in enumerate(arr):
        if num == 0:
            is_left_clear = (i - 1 < 0 or arr[i - 1] == 0) and (i - 2 < 0 or arr[i - 2] == 0)
            is_right_clear = (i + 1 >= len(arr) or arr[i + 1] == 0) and (i + 2 >= len(arr) or arr[i + 2] == 0)
            if is_left_clear and is_right_clear:
                arr[i] = 1
                maximum_seats += 1
    return maximum_seats


def test() -> None:
    # Expected: 2
    print(maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))

    # Expected: 2
    print(maximum_seating([0, 0, 0, 0]))

    # Expected: 1
    print(maximum_seating([1, 0, 0, 0, 0, 0, 0, 1]))


if __name__ == "__main__":
    test()
