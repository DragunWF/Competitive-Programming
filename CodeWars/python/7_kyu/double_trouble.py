# https://www.codewars.com/kata/57f7796697d62fc93d0001b8/train/python

def trouble(x: list[int], t: int) -> list[int]:
    while remove_trouble(x, t):
        pass
    return x


def remove_trouble(x: list[int], t: int) -> bool:
    for i in range(1, len(x)):
        prev, current = x[i - 1], x[i]
        if current + prev == t:
            x.pop(i)
            return True
    return False


def test() -> None:
    print(trouble([1, 2, 3, 4, 5], 3))
    print(trouble([2, 2, 2, 2, 2, 2], 4))


if __name__ == "__main__":
    test()
