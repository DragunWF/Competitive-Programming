# https://www.codewars.com/kata/5353212e5ee40d4694001114/train/python

def exchange_with(a: list, b: list) -> list:
    a.reverse()
    b.reverse()
    temp_a, temp_b = [*b], [*a]
    a.clear()
    b.clear()
    transfer_items(a, temp_a)
    transfer_items(b, temp_b)


def transfer_items(target: list, items: list) -> None:
    for item in items:
        target.append(item)


def test() -> None:
    exchange_with(['a', 'b', 'c'], [1, 2, 3])


if __name__ == "__main__":
    test()
