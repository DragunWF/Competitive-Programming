# https://www.codewars.com/kata/602db3215c22df000e8544f0/train/python

def two_are_positive(a: int, b: int, c: int) -> bool:
    return [n > 0 for n in [a, b, c]].count(True) == 2
