# https://www.codewars.com/kata/558c04ecda7fb8f48b000075/train/python

def same(arr_a: list, arr_b: list) -> bool:
    arr_a = [sorted(arr) for arr in arr_a]
    arr_b = [sorted(arr) for arr in arr_b]
    return sorted(arr_a) == sorted(arr_b)