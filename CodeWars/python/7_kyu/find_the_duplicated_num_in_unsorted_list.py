# https://www.codewars.com/kata/558dd9a1b3f79dc88e000001/train/python

def find_dup(arr: list[int]) -> int:
    for n in arr:
        if arr.count(n) >= 2:
            return n
