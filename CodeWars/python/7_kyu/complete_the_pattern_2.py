# https://www.codewars.com/kata/55733d3ef7c43f8b0700007c

def pattern(n: int) -> str:
    if n < 1:
        return ""
    output = []
    for i in range(n):
        row = []
        for j in range(n, 0 + i, -1):
            row.append(str(j))
        output.append("".join(row))
    return "\n".join(output)


def test() -> None:
    print(pattern(5))


if __name__ == "__main__":
    test()
