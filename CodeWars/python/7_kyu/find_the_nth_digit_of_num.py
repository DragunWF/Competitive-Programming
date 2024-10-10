# https://www.codewars.com/kata/577b9960df78c19bca00007e/python

def find_digit(num: int, nth: int) -> int:
    if nth <= 0:
        return -1
    if nth > len(str(num)):
        return 0
    return int(str(num)[-nth])
