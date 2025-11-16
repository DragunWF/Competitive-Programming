# https://www.codewars.com/kata/5a7893ef0025e9eb50000013

def max_gap(numbers: list) -> int:
    numbers.sort()
    max_gap = 0
    for i in range(1, len(numbers)):
        gap = numbers[i] - numbers[i - 1]
        if gap > max_gap:
            max_gap = gap
    return max_gap


def test() -> None:
    # Expected: 4
    print(max_gap([13, 10, 2, 9, 5]))


if __name__ == "__main__":
    test()
