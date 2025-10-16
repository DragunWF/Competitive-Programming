# https://www.codewars.com/kata/5592fc599a7f40adac0000a8

def sum_diagonals(matrix: list[list[int]]) -> int:
    total = 0
    N = len(matrix)
    right_diagonal_index = 0
    left_diagonal_index = N - 1
    for i in range(N):
        total += matrix[i][right_diagonal_index]
        total += matrix[i][left_diagonal_index]
        right_diagonal_index += 1
        left_diagonal_index -= 1
    return total


def test() -> None:
    # 30
    print(sum_diagonals(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ))


if __name__ == "__main__":
    test()
