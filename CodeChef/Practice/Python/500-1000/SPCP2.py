# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SPCP2

from math import ceil


class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x, n = util.ints()
            r = n - x * 100
            if r <= 0:
                print(0)
            else:
                print(ceil(r / 100))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
