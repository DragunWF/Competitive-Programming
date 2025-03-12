# https://www.codewars.com/kata/559656796d8fb52e17000003/train/python

def transpose(arr: list[list[int]]) -> list[list[int]]:
    matrix = []
    row_count = len(arr[0])
    for i in range(row_count):
        new_row = []
        for row in arr:
            new_row.append(row[i])
        matrix.append(new_row)
    return matrix
