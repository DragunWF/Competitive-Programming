# https://www.codewars.com/kata/55a75e2d0803fea18f00009d/train/python

def find_slope(points: list[int]) -> str:
    try:
        return str((points[3] - points[1]) // (points[2] - points[0]))
    except ZeroDivisionError:
        return "undefined"
