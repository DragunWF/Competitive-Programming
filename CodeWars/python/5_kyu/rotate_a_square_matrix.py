# https://www.codewars.com/kata/53fe3578d5679bf04900093f/train/python

def rotate_in_place(matrix: list[list[int]]):
    N = len(matrix)
    output = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(matrix[j][i])
        row.reverse()
        output.append(row)
    copy_matrix(matrix, output)
    return output


def copy_matrix(original_matrix: list[list[int]], new_matrix: list[list[int]]) -> None:
    N = len(original_matrix)
    for i in range(N):
        for j in range(N):
            original_matrix[i][j] = new_matrix[i][j]


def test() -> None:
    # [[7, 4, 1],
    #  [8, 5, 2],
    #  [9, 6, 3]]
    print(rotate_in_place(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    ))


if __name__ == "__main__":
    test()
