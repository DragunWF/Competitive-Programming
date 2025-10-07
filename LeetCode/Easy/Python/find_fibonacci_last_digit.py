# https://www.codewars.com/kata/56b7251b81290caf76000978/train/python


def get_last_digit(index: int):
    if index <= 1:
        return index

    prev = 0
    current = 1
    for i in range(2, index + 1):
        new_term = prev + current
        prev = current
        current = new_term
    return current % 10


def test() -> None:
    print(get_last_digit(15))  # 610 = 0


if __name__ == "__main__":
    test()
