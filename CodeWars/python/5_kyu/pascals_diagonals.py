# https://www.codewars.com/kata/576b072359b1161a7b000a17/train/python

def generate_diagonal(n: int, l: int) -> int:
    if l == 0:
        return []
    if n == 1:
        return [i for i in range(1, l + 1)]

    diagonal = [1]
    for i in range(1, l):
        diagonal.append(diagonal[i - 1] * (n + i) // i)
    return diagonal


def test() -> None:
    print(generate_diagonal(2, 5))  # [1, 3, 6, 10, 15]


if __name__ == "__main__":
    test()
