# https://www.codewars.com/kata/5263a84ffcadb968b6000513/train/python


def matrix_mult(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    N = len(a)
    b = transpose_matrix(b)
    b.reverse()

    result = []
    for i in range(N):
        row = []
        for j in range(N):
            cell = []
            for k in range(N):
                cell.append(a[i][k] * b[j][k])
            row.append(sum(cell))
        result.append(row)
    return result


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    N = len(matrix)
    transposed = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(matrix[j][i])
        transposed.insert(0, row)
    return transposed


def test() -> None:
    # [ [5, 4],
    #   [11, 8] ])
    print(matrix_mult(
          [[1, 2],
           [3, 2]],
          [[3, 2],
           [1, 1]]),)

    # [ [2, 1]
    #   [3, 1] ]
    print(transpose_matrix([[3, 2],
                            [1, 1]]))
    # [ [1, 1, 1]
    #   [5, 7, 8]
    #   [2, 6, 1] ]
    print(transpose_matrix([[2, 5, 1],
                            [6, 7, 1],
                            [1, 8, 1]]))


if __name__ == "__main__":
    test()
