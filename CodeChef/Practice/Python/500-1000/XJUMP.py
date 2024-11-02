# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/XJUMP

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x, y = util.ints()
            skips = x // y
            print((x - skips * y) + skips)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
