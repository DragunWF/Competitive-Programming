# https://www.codewars.com/kata/5a34da5dee1aae516d00004a/train/python

def get_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([0 if j != i else 1 for j in range(n)])
    return matrix
