# https://www.codewars.com/kata/56a13035eb55c8436a000041/train/python

from math import pi


def cup_volume(d1: int | float, d2: int | float, height: int | float) -> float:
    return (pi * height * (d1 ** 2 + d1 * d2 + d2 ** 2)) / 12
