# https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4/train/python

def least_larger(arr: list[int], i: int) -> int:
    target = arr[i]
    original = [*arr]
    arr.sort()
    for num in arr:
        if num > target:
            return original.index(num)
    return -1
