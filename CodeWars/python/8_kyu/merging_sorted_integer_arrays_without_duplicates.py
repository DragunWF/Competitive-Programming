# https://www.codewars.com/kata/573f5c61e7752709df0005d2/train/python

def merge_arrays(first: list[int], second: list[int]) -> list[int]:
    return sorted(list(set([*first, *second])))
