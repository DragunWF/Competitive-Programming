# https://www.codewars.com/kata/5727868888095bdf5c001d3d/train/python

def string_to_int_list(s: str) -> list[int]:
    return [int(n) for n in s.split(",") if n]