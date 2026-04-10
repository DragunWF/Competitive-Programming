# https://www.codewars.com/kata/5aa39ba75084d7cf45000008/train/python

def solve(n: int) -> str:
    sequence = ["0", "01"]
    if n <= 1:
        return sequence[n]
    for i in range(1, n):
        sequence.append(sequence[i] + sequence[i - 1])
    return sequence[-1]


def test() -> None:
    print(solve(3))


if __name__ == "__main__":
    test()
