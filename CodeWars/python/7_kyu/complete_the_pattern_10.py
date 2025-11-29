# https://www.codewars.com/kata/5581a7651185fe13190000ee

def pattern(n: int) -> str:
    output = []
    row = generate_row(n)
    for i in range(1, n + 1):
        output.append(f'{" " * (n - i)}{row}{" " * (i - 1)}')
    return "\n".join(output)


def generate_row(n: int) -> str:
    row = []
    for i in range(1, n + 1):
        row.append(str(i % 10))
    return "".join(row)


def test() -> None:
    print(pattern(5))


if __name__ == "__main__":
    test()

# '  123\n 123\n123' should equal '  123\n 123 \n123  '
