# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    array = set(array)
    return "{:.3f}".format(round(sum(array) / len(array), 3))
