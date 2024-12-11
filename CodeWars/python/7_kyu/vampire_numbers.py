# https://www.codewars.com/kata/54d418bd099d650fa000032d/train/python

from collections import Counter

def vampire_test(x: int, y: int) -> bool:
    return Counter(str(x) + str(y)) == Counter(str(x * y))