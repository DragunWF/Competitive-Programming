# https://www.codewars.com/kata/55ae997d1c40a199e6000018/train/python

def pattern(n: int) -> str:
    lines = []
    for i in range(n, 0, -1):
        line = []
        for j in range(n, 0, -1):
            if j > i:
                line.append(str(j % 10))
            else:
                line.append(str(i % 10))
        lines.append("".join(line))
    return "\n".join(lines)


def test() -> None:
    print(pattern(8))


if __name__ == "__main__":
    test()
