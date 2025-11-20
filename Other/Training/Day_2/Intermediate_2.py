import sys


def solve() -> None:
    n = int(input("N: "))
    sequence = generate_fibonacci(n)
    print("Sequence: ", sequence)


def generate_fibonacci(n: int) -> list[int]:
    seq = [0, 1]
    if n - 1 < len(seq):
        return seq[:n]
    for i in range(1, n - 1):
        seq.append(seq[i] + seq[i - 1])
    return seq


if __name__ == "__main__":
    solve()