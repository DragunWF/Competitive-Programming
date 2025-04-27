# https://www.codewars.com/kata/5a91e0793e9156ccb0003f6e/train/python

def matrixfy(s: str) -> list[list[str]]:
    if not s:
        return "name must be at least one letter"
    row_count = 1
    while row_count ** 2 < len(s):
        row_count += 1

    matrix, row = [], []
    for i in range(row_count ** 2):
        row.append(s[i] if i < len(s) else ".")
        if (i + 1) % row_count == 0:
            matrix.append([*row])
            row.clear()
    return matrix


def test() -> None:
    print(matrixfy("Marc"))
    print(matrixfy("Elaboration"))


if __name__ == "__main__":
    test()
