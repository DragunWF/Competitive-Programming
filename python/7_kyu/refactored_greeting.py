# https://www.codewars.com/kata/5121303128ef4b495f000001/train/python

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, name):
        return f"Hello {name}, my name is {self.name}"
