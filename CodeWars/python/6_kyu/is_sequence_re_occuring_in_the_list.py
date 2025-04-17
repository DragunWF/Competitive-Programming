# https://www.codewars.com/kata/5a7e6bd576c0e2f27d00237a/train/python

def is_reoccuring(items: list) -> bool:
    seen = set()
    prev = None
    for item in items:
        if item != prev:
            if item in seen:
                return True
            seen.add(item)
            prev = item
    return False


def test() -> None:
    data = [
        [0, 0, 1, 1, 0, 0],  # True
        [0, 0, 'a', 0],  # True
        [0, 0, 1, 1, 2, 2, 1, 1],  # True
        [0, 0, 0],  # False
        [0, 0, 1, 1, 2, 2]  # False
    ]
    for arr in data:
        print(is_reoccuring(arr))


if __name__ == "__main__":
    test()
