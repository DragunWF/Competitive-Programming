# https://www.codewars.com/kata/5ae326342f8cbc72220000d2/python

from string import digits


def string_expansion(s):
    first_digit = None
    output = ""
    for char in s:
        if char in digits:
            first_digit = int(char)
            continue
        if not char in digits:
            if not first_digit is None:
                if first_digit != 0:
                    output += char * first_digit
            else:
                output += char
    return output


def test():
    print(string_expansion("3D2a5d2f"))  # "DDDaadddddff"
    print(string_expansion("0d4n8d2b"))  # 'nnnnddddddddbb'
    print(string_expansion("7m3j4ik2a"))  # 'mmmmmmmjjjiiiikkkkaa'


if __name__ == '__main__':
    test()
