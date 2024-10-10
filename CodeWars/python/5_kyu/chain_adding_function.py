# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

class Number:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __eq__(self, other):
        return self.number == other

    def __add__(self, other):
        return self.number + other

    def __call__(self, value):
        if type(value) == Number:
            return Number(self.number + value.number)
        return Number(self.number + value)


def add(number):
    return Number(number)


def test():
    # Not part of the solution, just testing
    a = add(4)
    assert a == 4
    assert not (a == 5)
    b = a(a)


if __name__ == "__main__":
    test()
