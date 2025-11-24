# https://www.codewars.com/kata/557592fcdfc2220bed000042/train/python

def pattern(n: int) -> str:
    if n <= 0:
        return ""
    output = []
    selection = [str(i) for i in range(1, n + 1)]
    for i in range(n):
        row = []
        for j in range(n):
            current_index = (i + j) % n
            row.append(selection[current_index])
        output.append("".join(row))
    return "\n".join(output)


def test() -> None:
    print(pattern(9))


if __name__ == "__main__":
    test()
