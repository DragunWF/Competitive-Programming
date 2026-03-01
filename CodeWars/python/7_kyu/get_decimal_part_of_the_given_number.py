# https://www.codewars.com/kata/586e4c61aa0428f04e000069/train/python

def get_decimal(n: float) -> float:
    if n % 1 == 0:
        return 0
    return float("0." + str(n).split(".")[1])


def test() -> None:
    print(get_decimal(-1.2))


if __name__ == "__main__":
    test()
