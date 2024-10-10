# https://www.codewars.com/kata/5ffc226ce1666a002bf023d2

def solution(mtrx):
    for row in mtrx:
        if ">" in row and "x" in row:
            return True if row.index(">") < row.index("x") else False
    return False
