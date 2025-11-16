# https://www.codewars.com/kata/580435ab150cca22650001fb/train/python

def filter_lucky(arr: list) -> list:
    return list(filter(lambda item: "7" in str(item), arr))


def test() -> None:
    # Expected: [7,70,17]
    print(filter_lucky([1, 2, 3, 4, 5, 6, 7, 68, 69, 70, 15, 17]))


if __name__ == "__main__":
    test()
