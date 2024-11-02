# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFCAND

import math

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split(" "))
        if x >= n:
            print(0)
        else:
            print(math.ceil((n - x) / 4))
