# https://www.codewars.com/kata/595aa94353e43a8746000120/train/python

def find_deleted_number(arr: list[int], mixed_arr: list[int]) -> int:
    mixed_arr.sort()
    if arr == mixed_arr:
        return 0
    for i in range(len(arr)):
        if i >= len(mixed_arr) or arr[i] != mixed_arr[i]:
            return arr[i]
