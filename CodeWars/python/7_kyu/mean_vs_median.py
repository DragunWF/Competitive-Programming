# https://www.codewars.com/kata/5806445c3f1f9c2f72000031/train/python

def mean_vs_median(numbers: list[int]) -> str:
    N = len(numbers)
    numbers.sort()
    median = numbers[N // 2]
    mean = sum(numbers) / N
    if median == mean:
        return "same"
    return "mean" if mean > median else "median"


def test() -> None:
    print(mean_vs_median([1, 1, 1]))  # Same
    print(mean_vs_median([-10, 20, 5]))  # Same


if __name__ == "__main__":
    test()
