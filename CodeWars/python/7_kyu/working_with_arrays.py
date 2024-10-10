# https://www.codewars.com/kata/5a4ff3c5fd56cbaf9800003e/train/python

def without_last(lst):
    return [item for i, item in enumerate(lst) if i != len(lst) - 1]
