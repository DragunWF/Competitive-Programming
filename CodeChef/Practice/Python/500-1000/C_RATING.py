# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/C_RATING

from math import ceil


class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.num()
        for _ in range(t):
            x, y = util.ints()
            print(ceil((y - x) / 8))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
