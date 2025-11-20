import sys


def solve() -> None:
    matrix = input_matrix()
    print(get_matrix_sums(matrix))


def input_matrix() -> list[list[int]]:
    size = int(input("N: "))
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            num = int(input(f"Row: {i}, Column: {j}: "))
            row.append(num)
        matrix.append(row)
    return matrix


def get_matrix_sums(matrix: list[list[int]]) -> list[int]:
    output = []
    for row in matrix:
        output.append(sum(row))
    return output


if __name__ == "__main__":
    solve()