# https://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python

from math import sqrt


class Sudoku(object):
    def __init__(self, data: list[list[int]]):
        self.data = data
        self.row_len = len(data)

    def is_valid(self) -> bool:
        if self.row_len <= 0 or not self.is_board_square() or sqrt(self.row_len) % 1 != 0:
            return False
        if self.row_len == 1:
            return self.data[0][0] == 1
        return self.is_valid_rows() and self.is_valid_columns() and self.is_valid_squares()

    def is_board_square(self) -> bool:
        return max(len(row) for row in self.data) == self.row_len

    def is_valid_rows(self) -> bool:
        for row in self.data:
            if len(set(row)) != self.row_len:
                return False
        return True

    def is_valid_columns(self) -> bool:
        for i in range(self.row_len):
            column = set()
            for j in range(self.row_len):
                if not (1 <= self.data[j][i] <= self.row_len):
                    return False
                column.add(self.data[j][i])
            if len(column) != self.row_len:
                return False
        return True

    def is_valid_squares(self) -> bool:
        squares = [set() for i in range(self.row_len)]
        square_size = sqrt(self.row_len)
        for i in range(self.row_len):
            row_cycle = i // square_size * square_size
            for j in range(self.row_len):
                squares[int(j // square_size + row_cycle)].add(self.data[i][j])
        for square in squares:
            if len(square) != self.row_len:
                return False
        return True


def test() -> None:
    good_sudoku = Sudoku([
        [7, 8, 4, 1, 5, 9, 3, 2, 6],
        [5, 3, 9, 6, 7, 2, 8, 4, 1],
        [6, 1, 2, 4, 3, 8, 7, 5, 9],

        [9, 2, 8, 7, 1, 5, 4, 6, 3],
        [3, 5, 7, 8, 4, 6, 1, 9, 2],
        [4, 6, 1, 9, 2, 3, 5, 8, 7],

        [8, 7, 6, 3, 9, 4, 2, 1, 5],
        [2, 4, 3, 5, 6, 1, 9, 7, 8],
        [1, 9, 5, 2, 8, 7, 6, 3, 4]
    ])
    print(good_sudoku.is_valid())  # True

    bad_sudoku = Sudoku([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 1, 5, 6, 4, 8, 9, 7],
        [3, 1, 2, 6, 4, 5, 9, 7, 8],

        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 4, 8, 9, 7, 2, 3, 1],
        [6, 4, 5, 9, 7, 8, 3, 1, 2],

        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 7, 2, 3, 1, 5, 6, 4],
        [9, 7, 8, 3, 1, 2, 6, 4, 5]
    ])
    print(bad_sudoku.is_valid())  # False


if __name__ == "__main__":
    test()
