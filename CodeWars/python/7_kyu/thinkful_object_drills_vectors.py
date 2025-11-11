# https://www.codewars.com/kata/587f1e1f39d444cee6000ad4/train/python

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def subtract(self, vector):
        return Vector(self.y - vector.y, self.y - vector.y)
