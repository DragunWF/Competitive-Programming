import os
import sys
import itertools
import collections

def solve() -> None:
    n = int(input("Enter a number: "))
    line_count = 1
    while n > 0:
        line = []
        for i in range(line_count):
            line.append(n)
            n -= 1
        print(" ".join(str(n) for n in line))
        line_count += 1


if __name__ == "__main__":
    solve()