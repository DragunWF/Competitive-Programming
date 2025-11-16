# https://www.codewars.com/kata/5659c6d896bc135c4c00021e

from collections import Counter


def next_smaller(n: int) -> int:
    digits = list(str(n))
    length = len(digits)
    i = length - 2
    while i >= 0 and digits[i] <= digits[i + 1]:
        i -= 1
    if i < 0:
        return -1
    j = length - 1
    while digits[j] >= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = sorted(digits[i + 1:], reverse=True)
    result = int(''.join(digits))
    if len(str(result)) < length:
        return -1
    return result


def next_smaller_brute_force(n: int) -> int:
    if not is_valid_num(n):
        return -1

    initial_num_count = Counter(str(n))
    current_num = n - 1
    while initial_num_count != Counter(str(current_num)):
        current_num -= 1
    return current_num


def is_valid_num(n: int) -> bool:
    if n <= 9:
        return False
    str_num = str(n)
    if len(set(str_num)) == 1:
        return False
    str_num = "".join(digit for digit in str_num if digit != "0")
    for i in range(1, len(str_num)):
        if int(str_num[i - 1]) > int(str_num[i]):
            return True
    return False


def test() -> None:
    print(next_smaller(21))  # 12
    print(next_smaller(531))  # 513
    print(next_smaller(2071))  # 2017
    print(next_smaller(1234567908))  # 1234567890

    print(next_smaller(9))  # -1
    print(next_smaller(135))  # -1
    print(next_smaller(1027))  # -1


if __name__ == "__main__":
    test()
