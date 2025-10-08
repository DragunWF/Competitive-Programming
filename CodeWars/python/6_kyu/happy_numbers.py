# https://www.codewars.com/kata/5464cbfb1e0c08e9b3000b3e


def is_happy(n: int) -> bool:
    while True:
        if n == 1:
            return True
        elif n == 4:
            return False
        digits = str(n)
        digit_sum = 0
        for digit in digits:
            digit_sum += int(digit) ** 2
        n = digit_sum


def test() -> None:
    print(is_happy(7))  # True
    print(is_happy(3))  # False


if __name__ == "__main__":
    test()
