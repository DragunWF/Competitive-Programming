# https://www.codewars.com/kata/5589ad588ee1db3f5e00005a

def pattern(n: int) -> str:
    if n < 1:
        return ""
    lines = []
    whitespace = " " * (n - 1)
    for i in range(1, n):
        lines.append(f"{whitespace}{str(i % 10) * n}{whitespace}")
    middle_line = generate_middle_line(n)
    for i in range(n):
        lines.append(middle_line)
    for i in range(n - 1, 0, -1):
        lines.append(f"{whitespace}{str(i % 10) * n}{whitespace}")
    return "\n".join(lines)


def generate_middle_line(n: int) -> str:
    output = []
    for i in range(1, n):
        output.append(str(i % 10))
    output.append(str(n % 10) * n)
    for i in range(n - 1, 0, -1):
        output.append(str(i % 10))
    return "".join(output)


def test() -> None:
    print(pattern(5))
    print(pattern(11))


if __name__ == "__main__":
    test()
