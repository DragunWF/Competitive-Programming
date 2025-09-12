# https://www.codewars.com/kata/5a2e8c0955519e54bf0000bd/train/python

def check_digit(number: int, index1: int, index2: int, digit: int) -> bool:
    str_num = str(number)
    str_digit = str(digit)

    min_index = min(index1, index2)
    max_index = max(index1, index2)

    return str_digit in str_num[min_index:max_index + 1]


def test() -> None:
    print(check_digit(67845123654000, 4, 2, 5))  # True


if __name__ == "__main__":
    test()
