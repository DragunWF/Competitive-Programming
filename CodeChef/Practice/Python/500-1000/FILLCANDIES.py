# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FILLCANDIES

from math import ceil


class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            n, k, m = util.ints()
            print(ceil(n / (k * m)))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
