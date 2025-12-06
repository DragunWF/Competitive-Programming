# https://www.codewars.com/kata/5827e2efc983ca6f230000e0/train/python

def pattern(rows: int, columns: int, s: str) -> str:
    matrix = []
    current_str_index = 0
    for i in range(rows):
        row = []
        for j in range(columns):
            if current_str_index < len(s):
                row.append(s[current_str_index])
            else:
                row.append(" ")
            current_str_index += 1
        matrix.append(row)
    return convert_to_table(matrix)


def convert_to_table(matrix: list[list[str]]) -> str:
    lines = []
    border = []
    for i in range(len(matrix[0])):
        border.append("---")
    border = f'+{"+".join(border)}+'
    for row in matrix:
        lines.append(border)
        lines.append(f'| {" | ".join(row)} |')
    lines.append(border)
    return "\n".join(lines)


def test() -> None:
    print(pattern(4, 3, "Nice pattern"))


if __name__ == "__main__":
    test()
