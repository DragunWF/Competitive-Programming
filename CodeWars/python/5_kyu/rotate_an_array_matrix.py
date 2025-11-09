# https://www.codewars.com/kata/525a566985a9a47bc8000670/train/python

def rotate(matrix: list[list[int]], direction: str) -> str:
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix
    if direction == "clockwise":
        return clockwise(matrix)
    return counter_clockwise(matrix)


def clockwise(matrix: list[list[int]]) -> list[list[int]]:
    output = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            if j >= len(matrix):
                break
            row.append(matrix[j][i])
        row.reverse()
        output.append(row)
    return output


def counter_clockwise(matrix: list[list[int]]) -> list[list[int]]:
    output = []
    for i in range(len(matrix[0]) - 1, -1, -1):
        row = []
        for j in range(len(matrix)):
            if j >= len(matrix):
                break
            row.append(matrix[j][i])
        output.append(row)
    return output


def test() -> None:
    print(rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], "clockwise"))
    print(rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], "counter-clockwise"))
    print(rotate([[1, 2, 3]], "counter-clockwise"))


if __name__ == "__main__":
    test()
