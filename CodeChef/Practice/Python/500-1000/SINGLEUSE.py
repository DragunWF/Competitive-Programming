# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SINGLEUSE

from math import ceil


def solve() -> None:
    for _ in range(int(input())):
        h, x, y = map(int, input().split())
        print(ceil((h - y) / x) + 1)


if __name__ == "__main__":
    solve()
