# https://www.codewars.com/kata/5575ff8c4d9c98bc96000042/train/python

def pattern(n: int) -> str:
    if n <= 0:
        return ""
    output = []
    for i in range(1, n + 1):
        first_half = []
        for j in range(1, i):
            first_half.append(str(j % 10))
        second_half = []
        for j in range(i, 0, -1):
            second_half.append(str(j % 10))
        first_half = "".join(first_half)
        second_half = "".join(second_half)

        whitespace = " " * (n - i)
        output.append(f'{whitespace}{first_half}{second_half}{whitespace}')
    return "\n".join(output)


def test() -> None:
    print(pattern(5))
    print(pattern(20))


if __name__ == "__main__":
    test()
