# https://www.codewars.com/kata/58d3487a643a3f6aa20000ff/train/python

def min_min_max(arr: list) -> list:
    min_num = min(arr)
    max_num = max(arr)
    minimum_absent = None
    for num in range(min_num + 1, max_num):
        if not num in arr:
            minimum_absent = num
            break
    return [min_num, minimum_absent, max_num]


def test() -> None:
    print(min_min_max([-1, 4, 5, -23, 24]))  # [-23, -22, 24]
    print(min_min_max([1, 3, -3, -2, 8, -1]))  # [-3, 0, 8]
    print(min_min_max([2, -4, 8, -5, 9, 7]))  # [-5, -3, 9]


if __name__ == "__main__":
    test()
