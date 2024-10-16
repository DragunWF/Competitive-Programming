# https://www.codewars.com/kata/5421c6a2dda52688f6000af8/train/python

def compose(f, g):
    def func(*n):
        return f(g(n) if type(n) is int else g(sum(n)))
    return func
