# https://www.codewars.com/kata/55208f16ecb433c5c90001d2/train/python

def trace(matrix: list[list[int]]) -> int:
    rows = len(matrix)
    if not rows:
        return

    columns = len(matrix[0])
    if rows != columns:
        return

    total = 0
    for i in range(rows):
        total += matrix[i][i]
    return total
