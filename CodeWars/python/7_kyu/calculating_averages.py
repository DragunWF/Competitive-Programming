# https://www.codewars.com/kata/529f32794a6db5d32a00071f/train/python

class Calculator:
    @staticmethod
    def average(*args):
        if not args:
            return 0
        return sum(args) / len(args)