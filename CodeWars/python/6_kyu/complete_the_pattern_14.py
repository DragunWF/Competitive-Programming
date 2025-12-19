# https://www.codewars.com/kata/559379505c859be5a9000034

def pattern(n: int, y: int = 1, *args) -> str:
    if n < 1:
        return ""
    if y < 1:
        y = 1
    output = []
    for i in range(y):
        x_pattern = generate_x_pattern(n)
        for j, line in enumerate(x_pattern):
            if i != 0 and j == 0:
                continue
            output.append(line)
    return "\n".join(output)


def generate_x_pattern(n: int) -> list[str]:
    lines = []
    middle_whitespace_count = n * 2 - 3
    edge_whitespace_count = 0
    for i in range(1, n + 1):
        num = i % 10
        edges = " " * edge_whitespace_count
        if i != n:
            middle = " " * middle_whitespace_count
            lines.append(f"{edges}{num}{middle}{num}{edges}")
            middle_whitespace_count -= 2
            edge_whitespace_count += 1
        else:
            lines.append(f"{edges}{num}{edges}")
    for i in range(n - 1, 0, -1):
        middle_whitespace_count += 2
        edge_whitespace_count -= 1
        num = i % 10
        edges = " " * edge_whitespace_count
        middle = " " * middle_whitespace_count
        lines.append(f"{edges}{num}{middle}{num}{edges}")
    return lines


def test() -> None:
    print(pattern(3, 7))
    # print(pattern(5))
    # print("\n".join(generate_x_pattern(5)))


if __name__ == "__main__":
    test()
