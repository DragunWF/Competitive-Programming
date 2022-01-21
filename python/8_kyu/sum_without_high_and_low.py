# https://www.codewars.com/kata/576b93db1129fcf2200001e6

def sum_array(arr):
    if not arr or len(arr) < 2:
        return 0
    arr.pop(arr.index(min(arr))), arr.pop(arr.index(max(arr)))
    return sum(arr)
