# https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1/train/python

def array_madness(a: list[int], b: list[int]) -> bool:
    return sum([n ** 2 for n in a]) > sum([n ** 3 for n in b])
