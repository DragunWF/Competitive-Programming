# https://www.codewars.com/kata/59a1cdde9f922b83ee00003b/train/python

def stanton_measure(arr: list[int]) -> int:
    return arr.count(arr.count(1))


def test() -> None:
    # Expected: 3
    print(stanton_measure([1, 4, 3, 2, 1, 2, 3, 2]))


if __name__ == "__main__":
    test()
