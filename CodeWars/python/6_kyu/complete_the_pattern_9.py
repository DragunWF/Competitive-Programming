# https://www.codewars.com/kata/5579e6a5256bac65e4000060/train/python

def pattern(n: int) -> str:
    lines = []
    for i in range(1, n + 1):
        whitespace = " " * (n - i)
        lines.append(f"{whitespace}{generate_line(i)}{whitespace}")
    for i in range(n - 1, 0, -1):
        whitespace = " " * (n - i)
        lines.append(f"{whitespace}{generate_line(i)}{whitespace}")
    return "\n".join(lines)


def generate_line(n: int) -> str:
    output = []
    for i in range(1, n + 1):
        output.append(str(i % 10))
    for i in range(n - 1, 0, -1):
        output.append(str(i % 10))
    return "".join(output)


def test() -> None:
    print(pattern(5))


if __name__ == "__main__":
    test()
