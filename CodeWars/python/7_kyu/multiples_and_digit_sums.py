# https://www.codewars.com/kata/58ca77b9c0d640ecd2000b1e/train/python

def procedure(n: int) -> int:
    multiples = [n]
    for i in range(n + 1, 101):
        if i % n == 0:
            multiples.append(i)
    return sum(digit_sum(multiple) for multiple in multiples)


def digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(n))


def test() -> None:
    print(procedure(30))  # 18
    print(procedure(12))  # 72


if __name__ == "__main__":
    test()
