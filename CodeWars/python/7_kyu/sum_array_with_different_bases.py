# https://www.codewars.com/kata/5a005f4fba2a14897f000086/train/python

def sum_it_up(numbers_with_bases: list):
    total = 0
    for number, base in numbers_with_bases:
        total += int(number, base)
    return total


def test() -> None:
    print(sum_it_up([["101", 2], ["10", 8]]))  # 13
    print(sum_it_up([["ABC", 16], ["11", 2]]))  # 2751


if __name__ == "__main__":
    test()
