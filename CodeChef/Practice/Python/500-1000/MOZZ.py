# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MOZZ

from math import ceil

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y, r = map(int, input().split(" "))
        m = x + r // 30
        print(ceil(m / y))