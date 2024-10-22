# https://www.codewars.com/kata/5777fe3f355edbf0a5000d11/train/python

def x_marks_the_spot(mat: list[list[str]]) -> list:
    output = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "x":
                if output:
                    return []
                output = [i, j]
    return output
