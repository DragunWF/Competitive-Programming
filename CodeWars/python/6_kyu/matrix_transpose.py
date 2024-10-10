# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/python

def transpose(matrix: list[list[int]]) -> list[list[int]]:
    width, height = len(matrix[0]), len(matrix)
    output = [[] for i in range(width)]
    for i in range(height):
        for j in range(width):
            output[j].append(matrix[i][j])
    return output


def test() -> None:
    # Not part of the solution, just testing
    print(transpose([[1, 2, 3], [4, 5, 6]]))


if __name__ == '__main__':
    test()
