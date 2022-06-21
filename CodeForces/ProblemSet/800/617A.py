from math import ceil


def solve(x):
    return ceil(x / 5)


def main():
    x = int(input())
    print(solve(x))


main()
