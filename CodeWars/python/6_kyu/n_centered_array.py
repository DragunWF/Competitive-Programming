# https://www.codewars.com/kata/59b06d83cf33953dbb000010/train/python

def is_centered(xs: list[int], n: int) -> bool:
    N = len(xs)
    for i in range(N):
        current_sum = 0
        iterated_once = False
        for j in range(i, N - i):
            iterated_once = True
            current_sum += xs[j]
        if current_sum == n and (N % 2 == 0 or iterated_once):
            return True
    return False


def test() -> None:
    # Expected: True
    print(is_centered([3, 2, 10, 4, 1, 6, 9], 15))

    # Expected: True
    print(is_centered([1, 1, 15, -1, -1], 15))

    # Expected: False
    print(is_centered([1, 1, 15, -1, -1], 6))

    # Expected: False
    print(is_centered([2, 1, 2], 0))

    # Expected: True
    print(is_centered([25, 26, 23, 24], 0))


if __name__ == "__main__":
    test()
