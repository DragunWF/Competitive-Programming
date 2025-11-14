# https://www.codewars.com/kata/58df8b4d010a9456140000c7

from typing import Union


def palindrome(num: int) -> Union[int, str]:
    if type(num) is not int or num < 0:
        return "Not valid"

    lesser_palindrome = None
    higher_palindrome = None
    for current_num in range(num, 10, -1):
        if is_palindrome(current_num):
            lesser_palindrome = current_num
            break
    if lesser_palindrome == num:
        return num

    current_num = num + 1
    while not is_palindrome(current_num):
        current_num += 1
    higher_palindrome = current_num

    if lesser_palindrome is None:
        return higher_palindrome

    lesser_palindrome_distance = num - lesser_palindrome
    higher_palindrome_distance = higher_palindrome - num
    if higher_palindrome_distance <= lesser_palindrome_distance:
        return higher_palindrome
    return lesser_palindrome


def is_palindrome(num: int) -> bool:
    str_num = str(num)
    if len(str_num) == 1:
        return False
    return str_num == str_num[::-1]


def test() -> None:
    print(palindrome(8))  # => 11
    print(palindrome(281))  # => 282
    print(palindrome(1029))  # => 1001
    print(palindrome(1221))  # => 1221
    print(palindrome("1221"))  # => "Not valid"
    print(palindrome(611))  # => 616


if __name__ == "__main__":
    test()
