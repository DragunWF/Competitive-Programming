# https://www.codewars.com/kata/691ca4c58c5f7e662d508d31


def find_saddle_points(matrix: list[list[int]]) -> list[tuple[int, int]]:
    saddle_points = []
    columns = transpose_matrix(matrix)
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if max(columns[j]) == column and min(row) == column:
                saddle_points.append((i, j))
    return saddle_points


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    column_matrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        column_matrix.append(row)
    return column_matrix


def test() -> None:
    # Expected: [(0, 2), (3,2)]
    matrix = [
        [6, 4, 3],
        [7, 0, 2],
        [4, 3, 2],
        [5, 3, 3]
    ]
    print(find_saddle_points(matrix))
    print(transpose_matrix(matrix))


if __name__ == "__main__":
    test()
