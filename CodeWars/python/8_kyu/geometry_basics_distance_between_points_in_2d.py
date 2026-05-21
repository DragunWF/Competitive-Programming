# https://www.codewars.com/kata/58dced7b702b805b200000be/train/python

from math import sqrt


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def distance_between_points(a: Point, b: Point) -> int:
    return sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))
