# https://www.codewars.com/kata/58df62fe95923f7a7f0000cc

from typing import Union


def palindrome(num: int) -> Union[int, str]:
    if type(num) is not int or num < 0:
        return "Not valid"
    if num <= 9:
        return 0

    str_num = str(num)
    end_pointer = len(str_num) - 1
    palindrome_count = 0
    while end_pointer > 0:
        for pointer in range(end_pointer + 1):
            substring = str_num[pointer:end_pointer + 1]
            if len(substring) == 1:
                break
            if substring == substring[::-1]:
                palindrome_count += 1
        end_pointer -= 1
    return palindrome_count


def test() -> None:
    print(palindrome(5))  # => 0
    print(palindrome(1221))  # => 2
    print(palindrome(141221001))  # => 5
    print(palindrome(1294))  # => 0
    print(palindrome("1221"))  # => "Not valid"


if __name__ == "__main__":
    test()
