# https://www.codewars.com/kata/59c7e477dcc40500f50005c7/train/python

def is_odd_heavy(arr: list[int]) -> bool:
    odd_nums = [num for num in arr if num % 2 != 0]
    if not odd_nums:
        return False
    min_odd_num = min(odd_nums)
    return all(min_odd_num > num for num in arr if num % 2 == 0)


def test() -> None:
    print(is_odd_heavy([11, 4, 9, 2, 8]))  # True


if __name__ == "__main__":
    test()
