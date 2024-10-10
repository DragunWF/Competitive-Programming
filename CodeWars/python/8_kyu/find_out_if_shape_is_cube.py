# https://www.codewars.com/kata/58d248c7012397a81800005c/train/python

def cube_checker(volume: int, side: int) -> bool:
    return not side <= 0 and side * side * side == volume 