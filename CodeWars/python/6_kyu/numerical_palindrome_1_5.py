# https://www.codewars.com/kata/58e09234ca6895c7b300008c

from typing import Union


def palindrome(num: int, s: int) -> Union[list[int], str]:
    if not is_valid(num) or not is_valid(s):
        return "Not valid"
    if s == 0:
        return []
    output = []
    current_num = max(num, 11)
    while len(output) < s:
        if is_palindrome(current_num):
            output.append(current_num)
        current_num += 1
    return output


def is_valid(value: int) -> bool:
    return type(value) is int and value >= 0


def is_palindrome(num: int) -> bool:
    str_num = str(num)
    return str_num[::-1] == str_num


def test() -> None:
    print(palindrome(6, 4))  # => [11,22,33,44]
    print(palindrome(59, 3))  # => [66,77,88]
    print(palindrome(101, 2))  # => [101,111]
    print(palindrome("15651", 5))  # => "Not valid"
    print(palindrome(1221, "8"))  # => "Not valid"


if __name__ == "__main__":
    test()
