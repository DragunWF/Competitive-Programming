# https://www.codewars.com/kata/54582f970a80d2ca46000f25/train/ruby

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self) -> str:
        return f"Hello, {self.first_name} {self.last_name}!"
