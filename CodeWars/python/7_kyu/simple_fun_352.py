# https://www.codewars.com/kata/59c8b38423dacc7d95000008/train/python

def is_valid(formula: list[int]) -> int:
    # Waw...
    if 1 in formula and 2 in formula:
        return False
    if 3 in formula and 4 in formula:
        return False
    if (5 in formula or 6 in formula) and not (5 in formula and 6 in formula):
        return False
    if not (7 in formula or 8 in formula):
        return False
    return True


def test() -> None:
    print(is_valid([7, 1, 2, 3]))


if __name__ == "__main__":
    test()
