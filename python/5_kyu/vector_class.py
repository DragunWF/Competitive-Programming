# https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4/train/python

from math import sqrt


class Vector:
    def __init__(self, values):
        self.values = values
        self.length = len(values)

    def add(self, vector):
        if self.length != vector.length:
            raise Exception()
        return Vector([self.values[i] + vector.values[i] for i in range(self.length)])

    def subtract(self, vector):
        if self.length != vector.length:
            raise Exception()
        return Vector([self.values[i] - vector.values[i] for i in range(self.length)])

    def dot(self, vector):
        if self.length != vector.length:
            raise Exception()
        return sum([self.values[i] * vector.values[i] for i in range(self.length)])

    def equals(self, vector):
        if self.length != vector.length:
            return False
        return all([self.values[i] == vector.values[i] for i in range(self.length)])

    def norm(self):
        return sqrt(sum([self.values[i] ** 2 for i in range(self.length)]))

    def __str__(self):
        return f"({','.join(list(map(str, self.values)))})"
