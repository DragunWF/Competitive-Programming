# https://www.codewars.com/kata/68851563123e161332d2a84b/train/python

def has_loop(arr: list[int]) -> bool:
    seen = set()
    i = 0
    while i < len(arr):
        next_index = arr[i]
        if next_index in seen:
            return True
        seen.add(next_index)
        i = next_index
    return False


def test() -> None:
    print(has_loop([1, 2, 3, 4, 2]))  # True
    print(has_loop([1, 2, 3, 4, 5]))  # False


if __name__ == "__main__":
    test()
