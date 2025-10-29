# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WATERCOOLER2

from math import ceil


def solve() -> None:
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(ceil(y / x) - 1)


if __name__ == "__main__":
    solve()
