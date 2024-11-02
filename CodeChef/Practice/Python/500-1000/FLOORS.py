# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOORS

from math import ceil


class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x, y = util.ints()
            print(abs(int(ceil(x / 10) - ceil(y / 10))))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
