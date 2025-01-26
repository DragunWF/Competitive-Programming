# https://www.codewars.com/kata/582c81d982a0a65424000201/train/python

def arr_check(arr: list) -> bool:
    return all(type(item) is list for item in arr)
