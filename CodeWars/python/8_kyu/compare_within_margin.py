# https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/python

def close_compare(a: int, b: int, margin=None) -> int:
    absolute_distance = abs(a - b)
    if (not margin is None and margin >= absolute_distance) or a == b:
        return 0
    return 1 if a > b else -1


def test() -> None:
    # Expected: -1
    print(close_compare(4, 5))
    # Expected: 1
    print(close_compare(8.1, 5, 3))


if __name__ == "__main__":
    test()
