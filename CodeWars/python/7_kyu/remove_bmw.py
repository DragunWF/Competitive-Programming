# https://www.codewars.com/kata/59de795c289ef9197f000c48/python

def remove_bmw(s: str) -> str:
    if not type(s) is str:
        raise TypeError("This program only works for text.")
    return "".join(char for char in s if not char in "bmwBMW")


def test() -> None:
    print(remove_bmw("bmwvolvoBMW"))


if __name__ == "__main__":
    test()
