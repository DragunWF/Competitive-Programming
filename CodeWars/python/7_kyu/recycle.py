# https://www.codewars.com/kata/59fb783bab11f89202001083/train/python

def recycle_me(rubbish: list[int]) -> tuple[int, int, int]:
    plastic, glass, card = 0, 0, 0
    for garbage in rubbish:
        if garbage > 0:
            plastic += 1
        elif garbage < 0:
            glass += 1
        else:
            card += 1
    return (plastic, glass, card)


def test() -> None:
    print(recycle_me([5, -9, 0, 6, -84, -95, 15]))


if __name__ == "__main__":
    test()
