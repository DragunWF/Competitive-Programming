# https://www.codewars.com/kata/55c7f90ac8025ebee1000062/train/python

def sort_array(value: str) -> str:
    return "".join(sorted(value, key=lambda a: int(a)))
