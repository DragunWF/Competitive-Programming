# https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python

from math import sqrt


def heron(a: int, b: int, c: int) -> float:
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))
