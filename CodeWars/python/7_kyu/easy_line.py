# https://www.codewars.com/kata/56e7d40129035aed6c000632

def easyline(n: int) -> int:
    return sum([cell ** 2 for cell in get_pascal_row(n)])


def get_pascal_row(line_number: int):
    if line_number < 0:
        return []

    row_index = line_number
    row = []
    C = 1
    for k in range(row_index + 1):
        row.append(C)
        C = C * (row_index - k) // (k + 1)
    return row


def test() -> None:
    print(easyline(0))  # 1
    print(easyline(4))  # 70
    print(get_pascal_row(3))  # [1, 2, 1]


if __name__ == "__main__":
    test()
