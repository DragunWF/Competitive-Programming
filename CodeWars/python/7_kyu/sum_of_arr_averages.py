# https://www.codewars.com/kata/56d5166ec87df55dbe000063/train/python

def sum_average(arr: list[list[int]]):
    return (sum(sum(i) / len(i) for i in arr)).__floor__()
