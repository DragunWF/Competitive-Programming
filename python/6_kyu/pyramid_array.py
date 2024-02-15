# https://www.codewars.com/kata/515f51d438015969f7000013/train/python

def pyramid(n):
    return [[1 for j in range(i + 1)] for i in range(n)]


# test code
print(pyramid(3))
