# https://www.codewars.com/kata/57be6a612eaf7cc3af000178/train/python

def is_magical(square: list[int]) -> bool:
    matrix = convert_to_matrix(square)
    row_sums = get_row_sums(matrix)
    column_rows = get_column_rows(matrix)
    return len(set([*row_sums, *column_rows])) == 1


def convert_to_matrix(square: list[int]) -> list[list[int]]:
    matrix = []
    row = []
    for i, num in enumerate(square):
        row.append(num)
        if (i + 1) % 3 == 0:
            matrix.append(row.copy())
            row.clear()
    return matrix


def get_row_sums(matrix: list[list[int]]) -> list[int]:
    return [sum(row) for row in matrix]


def get_column_rows(matrix: list[list[int]]) -> list[int]:
    output = []
    for i in range(len(matrix)):
        column = []
        for j in range(len(matrix)):
            column.append(matrix[j][i])
        output.append(sum(column))
    return output


def test() -> None:
    print(is_magical([4, 9, 2, 3, 5, 7, 8, 1, 6]))  # True


if __name__ == "__main__":
    test()
