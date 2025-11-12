# https://www.codewars.com/kata/55c11989e13716e35f000013/train/python

from collections import deque


def add(a, b):
    max_digit_count = max(len(a), len(b))
    if len(a) < max_digit_count:
        a = pad_zeros(a, max_digit_count)
    if len(b) < max_digit_count:
        b = pad_zeros(b, max_digit_count)
    output = deque([])
    carry_one = False

    for i in range(-1, -(max_digit_count + 1), -1):
        bit_a = a[i] == '1'
        bit_b = b[i] == '1'
        sum_bits = bit_a + bit_b + carry_one

        if sum_bits == 0:
            output.appendleft('0')
            carry_one = False
        elif sum_bits == 1:
            output.appendleft('1')
            carry_one = False
        elif sum_bits == 2:
            output.appendleft('0')
            carry_one = True
        else:  # sum_bits == 3
            output.appendleft('1')
            carry_one = True

    if carry_one:
        output.appendleft('1')

    result = ''.join(output)
    result = result.lstrip('0') or '0'

    return result


def pad_zeros(value, required_digits):
    return (required_digits - len(value)) * "0" + value


def add_old(a: str, b: str) -> str:
    max_digit_count = max(len(a), len(b))
    if len(a) < max_digit_count:
        a = pad_zeros(a, max_digit_count)
    if len(b) < max_digit_count:
        b = pad_zeros(b, max_digit_count)
    output = deque([])
    carry_one = False
    for i in range(-1, -(max_digit_count + 1), -1):
        result = int(a[i]) + int(b[i])
        if carry_one:
            result += 1
            carry_one = False
        if result >= 2:
            carry_one = True
        output.appendleft(str(result % 2))
    if carry_one:
        output.appendleft("1")
    return str(int("".join(output)))


def test() -> None:
    print(add('111', '10'))  # => '1001'
    print(add('1101', '101'))  # => '10010'
    print(add('1101', '10111'))  # => '100100'


if __name__ == "__main__":
    test()
