# https://www.codewars.com/kata/52988f3f7edba9839c00037d/train/python

def reject(seq: list, predicate) -> list:
    return list(filter(lambda item: not predicate(item), seq))


def test() -> None:
    print(reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))  # [1, 3, 5]


if __name__ == "__main__":
    test()
