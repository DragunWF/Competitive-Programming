# https://www.codewars.com/kata/5a036ecb2b651d696f00007c/train/python

def draw_a_cross(n: int) -> str:
    if n < 3:
        return "Not possible to draw cross for grids less than 3x3!"
    if n % 2 == 0:
        return "Centered cross not possible!"

    first_half = []
    for i in range(n // 2):
        row = get_row(n)
        row[i] = "x"
        row[-1 - i] = "x"
        first_half.append("".join(row))

    middle_row = get_row(n)
    middle_row[n // 2] = "x"
    middle_row = "".join(middle_row)

    second_half = list(reversed([*first_half]))
    cross = [*first_half, middle_row, *second_half]

    return "\n".join(cross)


def get_row(n: int) -> str:
    return [*(" " * n)]


def test() -> None:
    print(draw_a_cross(7))
    print(draw_a_cross(15))


if __name__ == "__main__":
    test()
