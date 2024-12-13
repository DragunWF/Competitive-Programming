# https://www.codewars.com/kata/59a9919107157a45220000e1/train/python

def find_all(array, target):
    return [i for i, num in enumerate(array) if num == target]
