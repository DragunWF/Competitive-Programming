# https://www.codewars.com/kata/586ec0b8d098206cce001141/train/python

def inverse_slice(items: list, a: int, b: int) -> list:
    sliced = []
    for i, item in enumerate(items):
        if not (a <= i < b):
            sliced.append(item)
    return sliced


def test() -> None:
    # [12, 14, 55, 24]
    print(inverse_slice([12, 14, 63, 72, 55, 24], 2, 4))


if __name__ == "__main__":
    test()
