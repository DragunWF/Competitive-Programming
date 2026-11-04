# https://www.codewars.com/kata/57785441311a24465e000025/train/python

def make_checkered_board(n):
    board = []
    row = []
    for i in range(1, n + 1):
        first_cell = None
        second_cell = None
        if i % 2 != 0:
            first_cell = "X"
            second_cell = "O"
        else:
            first_cell = "O"
            second_cell = "X"
        for j in range(1, n + 1):
            row.append(second_cell if j % 2 == 0 else first_cell)
        board.append([*row])
        row.clear()
    return board