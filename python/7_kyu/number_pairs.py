# https://www.codewars.com/kata/563b1f55a5f2079dc100008a/train/python

def get_larger_numbers(a, b):
    return [max(a[i], b[i]) for i in range(len(a))]
