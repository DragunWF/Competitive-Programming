# https://www.codewars.com/kata/528d9adf0e03778b9e00067e/train/python

def mine_location(field: list[list[int]]) -> list[int]:
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                return [i, j]
