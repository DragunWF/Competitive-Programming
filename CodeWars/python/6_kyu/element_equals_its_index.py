# https://www.codewars.com/kata/5b7176768adeae9bc9000056

def index_equals_value(arr: list[int]) -> list:
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            right = mid - 1
            result = mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return result


def test() -> None:
    print(index_equals_value([-8, 0, 2, 5]))  # 2


if __name__ == "__main__":
    test()
