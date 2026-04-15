# https://www.codewars.com/kata/52af1f150fcae8d33d0009bc/train/python

def ho(value: str = "") -> str:
    if not value:
        return "Ho!"
    value = value[:-1]
    return f"Ho {value}!"


def test() -> None:
    print(ho())         # should return "Ho!"
    print(ho(ho()))     # should return "Ho Ho!"
    print(ho(ho(ho())))  # should return "Ho Ho Ho!"


if __name__ == "__main__":
    test()
