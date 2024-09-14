# https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python

def calc(s: str) -> int:
    str_num = ""
    for char in s:
        str_num += str(ord(char))
    return sum_digits(str_num) - sum_digits(str_num.replace("7", "1"))

def sum_digits(str_num: str) -> int:
    return sum(int(n) for n in str_num)


def test():
    # Not part of the solution
    print(calc("abcdef"))


if __name__ == "__main__":
    test()