# https://www.codewars.com/kata/5574940eae1cf7d520000076/train/python

def pattern(n: int) -> str:
    output = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            output.append(f"{i}" * i)
    return "\n".join(output)


def test() -> None:
    print(pattern(5))


if __name__ == "__main__":
    test()
