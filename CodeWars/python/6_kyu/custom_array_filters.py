# https://www.codewars.com/kata/53fc954904a45eda6b00097f/train/python

import builtins


class list(builtins.list):
    def even(self):
        return [n for n in self if type(n) is int and n % 2 == 0]

    def odd(self):
        return [n for n in self if type(n) is int and n % 2 != 0]

    def under(self, target: int):
        return [n for n in self if type(n) is int and n < target]

    def over(self, target: int):
        return [n for n in self if type(n) is int and n > target]

    def in_range(self, start: int, end: int):
        return [n for n in self if type(n) is int and start <= n <= end]


def test():
    values = [1, 2, 3, 4, 5]
    print(list(values).even())


if __name__ == "__main__":
    test()
