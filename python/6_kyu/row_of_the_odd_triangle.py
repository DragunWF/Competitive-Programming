# https://www.codewars.com/kata/5d5a7525207a674b71aa25b5/train/python

def odd_row(n: int):
    output = []
    limit = int((n * (n + 1)) / 2)
    num = 1 + 2 * (limit - 1)
    for i in range(n):
        output.append(num)
        num -= 2
    output.reverse()
    return output


def test():
    # Not part of the solution, just testing
    TEST_CASES = 5
    for num in range(1, TEST_CASES + 1):
        print(odd_row(num))


if __name__ == "__main__":
    test()