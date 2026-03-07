# https://www.codewars.com/kata/5a043724ffe75fbab000009f/train/python

def reverse_middle(items: list) -> list:
    middle = len(items) // 2
    if len(items) % 2 == 0:
        return [items[middle], items[middle - 1]]
    return list(reversed(items[middle - 1: middle + 2]))


def test() -> None:
    print(reverse_middle([4, 3, 100, 1]))  # [100, 3]
    print(reverse_middle([1, False, 'string', {}, 7.43]))  # [{}, 'string', False]


if __name__ == "__main__":
    test()
