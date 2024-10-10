# https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/train/python

def fix_the_meerkat(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr
