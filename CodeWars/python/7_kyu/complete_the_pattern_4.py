# https://www.codewars.com/kata/55736129f78b30311300010f

def pattern(n: int) -> str:
    if n <= 0:
        return ""
    output = []
    for i in range(1, n + 1):
        row = []
        for j in range(i, n + 1):
            row.append(str(j))
        output.append("".join)
    return "\n".join(output)


def test() -> None:
    print(pattern(5))


if __name__ == "__main__":
    test()
