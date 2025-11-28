# https://www.codewars.com/kata/55749101ae1cf7673800003e

def pattern(n: int) -> str:
    if n <= 1:
        return ""
    output = []
    for i in range(2, n + 1, 2):
        output.append(str(i) * i)
    return "\n".join(output)


def test() -> None:
    print(pattern(8))


if __name__ == "__main__":
    test()
