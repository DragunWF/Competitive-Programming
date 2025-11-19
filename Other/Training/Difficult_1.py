import sys


def solve() -> None:
    sudoku_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    sudoku(sudoku_board, 0, 0)
    for row in sudoku_board:
        sys.stdout.write(" ".join(str(n) for n in row) + "\n")


def sudoku(matrix: list[int], row: int, col: int) -> list[int]:
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if matrix[row][col] != 0:
        return sudoku(matrix, row, col + 1)

    for num in range(1, 10):
        if is_safe(matrix, row, col, num):
            matrix[row][col] = num
            if sudoku(matrix, row, col + 1):
                return True
            matrix[row][col] = 0

    return False


def is_safe(matrix: list[int], row: int, col: int, num: int) -> bool:
    for x in range(9):
        if matrix[row][x] == num:
            return False

    for x in range(9):
        if matrix[x][col] == num:
            return False

    startRow = row - (row % 3)
    startCol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if matrix[i + startRow][j + startCol] == num:
                return False

    return True


if __name__ == "__main__":
    solve()
