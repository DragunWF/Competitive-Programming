# https://www.codewars.com/kata/5919f3bf6589022915000023/train/python

def rotate_against_clockwise(matrix: list[list[int]], times: int) -> list:
    rotations = 0
    while rotations < times % 4:
        matrix = rotate_in_place(matrix)
        rotations += 1
    return matrix


def rotate_in_place(matrix: list[list[int]]) -> list[list[int]]:
    N = len(matrix)
    output = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(matrix[j][i])
        output.append(row)
    output.reverse()
    return output


def test() -> None:
    # [[4, 8, 12, 16],
    # [3, 7, 11, 15],
    # [2, 6, 10, 14],
    # [1, 5, 9, 13]])
    print(rotate_against_clockwise(
          [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]], 1))


if __name__ == "__main__":
    test()
