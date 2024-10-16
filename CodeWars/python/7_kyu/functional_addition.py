# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python

def add(n: int):
    def func(other_n: int):
        return n + other_n
    return func
