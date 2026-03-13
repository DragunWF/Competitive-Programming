# https://www.codewars.com/kata/5a8897d4ba1bb5f266000057/train/python

def make_2d_list(head: int, row: int, col: int) -> list[list[int]]:
    matrix = []
    current_num = head
    for i in range(row):
        current_row = []
        for j in range(col):
            current_row.append(current_num)
            current_num += 1
        matrix.append(current_row)
    return matrix


def test() -> None:
    print(make_2d_list(1, 2, 3))  # [[1, 2, 3], [4, 5, 6]]


if __name__ == "__main__":
    test()
