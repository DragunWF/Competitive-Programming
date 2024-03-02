# https://www.codewars.com/kata/5899642f6e1b25935d000161/train/python

def merge_arrays(arr1, arr2):
    return sorted(list(set([*arr1, *arr2])))
