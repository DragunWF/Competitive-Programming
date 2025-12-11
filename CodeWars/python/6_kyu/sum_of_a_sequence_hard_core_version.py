# https://www.codewars.com/kata/587a88a208236efe8500008b/train/python

def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    n = (end_number - begin_number) // step + 1
    if n <= 0:
        return 0
    return (n * (2 * begin_number + (n - 1) * step)) // 2


def test() -> None:
    # 12 (= 2 + 4 + 6)
    print(sequence_sum(2, 6, 2))


if __name__ == "__main__":
    test()
