# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MYSERVE

from math import floor


class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            p, q = util.ints()
            print("Alice" if (floor((p + q) / 2) + 1) % 2 != 0 else "Bob")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
