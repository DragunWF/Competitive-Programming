# https://www.codewars.com/kata/67fb86b6564f0bd70dc615b1/train/python

def validate_euro(serial_number: str) -> bool:
    serial_sum = 0
    for char in serial_number:
        if char.isdigit():
            serial_sum += int(char)
        else:
            serial_sum += ord(char) - 64

    while len(str(serial_sum)) != 1:
        digit_sum = 0
        for digit in str(serial_sum):
            digit_sum += int(digit)
        serial_sum = digit_sum
    return serial_sum == 7


def test() -> None:
    print(validate_euro("VA0436214792"))  # True
    print(validate_euro("UB5067129430"))  # False


if __name__ == "__main__":
    test()
