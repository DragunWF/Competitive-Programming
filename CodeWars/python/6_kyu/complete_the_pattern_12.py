# https://www.codewars.com/kata/558ac25e552b51dbc60000c3/train/python

def pattern(n: int) -> str:
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
    return "\n".join(lines)


def test() -> None:
    print(pattern(5))
    print(pattern(10))


if __name__ == "__main__":
    test()
