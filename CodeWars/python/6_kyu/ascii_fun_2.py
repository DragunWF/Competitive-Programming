# https://www.codewars.com/kata/ascii-fun-number-2-funny-dots

def dot(n: int, m: int) -> str:
    lines = []
    border = generate_border(n)
    cells = generate_cells(n)
    lines.append(border)
    for i in range(m):
        lines.append(cells)
        lines.append(border)
    return "\n".join(lines)


def generate_border(n: int) -> str:
    content = ["---" for i in range(n)]
    return f"+{'+'.join(content)}+"


def generate_cells(n: int) -> str:
    content = [" o " for i in range(n)]
    return f"|{'|'.join(content)}|"


def test() -> None:
    print(dot(3, 2))


if __name__ == "__main__":
    test()
