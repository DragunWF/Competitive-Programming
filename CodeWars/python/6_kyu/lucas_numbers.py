# https://www.codewars.com/kata/55a7de09273f6652b200002e/python

def lucasnum(n: int) -> int:
    if n == 0:
        return 2
    elif n == 1 or n == -1:
        return n

    is_positive = n > 0
    prev = 2
    current = 1
    for i in range(2, abs(n) + 1):
        new_term = prev + current
        prev = current
        current = new_term
    if is_positive:
        return current
    return -current if n % 2 != 0 else current


def test() -> None:
    print(lucasnum(0))  # 2
    print(lucasnum(5))  # 11
    print(lucasnum(10))  # 123


if __name__ == "__main__":
    test()
