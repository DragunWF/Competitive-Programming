# https://www.codewars.com/kata/5834315e06f227a6ac000099/train/python

def elimination(arr: list[int]) -> int | None:
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return arr[i]
