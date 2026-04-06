# https://www.codewars.com/kata/55a5c82cd8e9baa49000004c/train/python

def divisible_count(x: int, y: int, k: int) -> int:
    start, end = min(x, y), max(x, y)
    return (end // k) - ((start - 1) // k)


def test() -> None:
    print(divisible_count(6, 11, 2))  # 3
    print(divisible_count(0, 1, 7))  # 1
    print(divisible_count(20, 20, 2))  # 1
    print(divisible_count(20, 20, 8))  # 0


if __name__ == "__main__":
    test()
