# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python
from rich import print


def valid_solution(board: list) -> bool:
    columns = []
    for i in range(9):  # Board will always be 9x9
        column = []
        for j in range(9):
            if board[j][i] == 0:
                return False
            column.append(board[j][i])
        columns.append(column)

    blocks, quarter = [], []
    for i in range(9):
        quarter.append(board[i])
        if ((i + 1) % 3) == 0:
            quarter_blocks = get_quarter_blocks(quarter)
            for block in quarter_blocks:
                blocks.append(block)
            quarter = []

    return validate(board) and validate(columns) and validate(blocks)


def get_quarter_blocks(quarter: list) -> list:
    blocks, block = [], []
    for i in range(len(quarter)):
        for j in range(3):  # 3x3 block
            block.append(quarter[j][i])
        if ((i + 1) % 3) == 0:
            blocks.append(block)
            block = []
    return blocks


def validate(board: list) -> bool:
    for row in board:
        if len(set(row)) != 9:
            return False
    return True


def test():
    test_cases = [
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ],  # True
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 0, 3, 4, 8],
            [1, 0, 0, 3, 4, 2, 5, 6, 0],
            [8, 5, 9, 7, 6, 1, 0, 2, 0],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 0, 1, 5, 3, 7, 2, 1, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 0, 0, 4, 8, 1, 1, 7, 9]
        ],  # False
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]  # False
    ]
    for case in test_cases:
        print(valid_solution(case))


if __name__ == "__main__":
    test()
