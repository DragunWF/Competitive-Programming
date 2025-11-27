# https://www.codewars.com/kata/557341907fbf439911000022/train/python

def pattern(n: int) -> str:
    output = []
    for i in range(n - 1, -1, -1):
        row = []
        for j in range(n, i, -1):
            row.append(str(j))
        output.append("".join(row))
    return "\n".join(output)


def test() -> None:
    print(pattern(5))


if __name__ == "__main__":
    test()
