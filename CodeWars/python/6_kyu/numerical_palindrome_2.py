# https://www.codewars.com/kata/58de819eb76cf778fe00005c


def palindrome(num: int):
    if type(num) is not int or num < 0:
        return "Not valid"
    if num <= 9:
        return False

    str_num = str(num)
    end_pointer = len(str_num) - 1
    while end_pointer > 0:
        for pointer in range(end_pointer + 1):
            substring = str_num[pointer: end_pointer + 1]
            if len(substring) == 1:
                break
            if substring == substring[::-1]:
                return True
        end_pointer -= 1
    return False


def test() -> None:
    print(palindrome(5))  # => false
    print(palindrome(1221))  # => true
    print(palindrome(141221001))  # => true
    print(palindrome(1215))  # => true
    print(palindrome(1294))  # => false
    print(palindrome("109982"))  # => "Not valid"


if __name__ == "__main__":
    test()
