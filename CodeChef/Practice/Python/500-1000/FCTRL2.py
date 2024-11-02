# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FCTRL2

from math import factorial

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.num()
        for _ in range(t):
            n = util.num()
            print(factorial(n))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
