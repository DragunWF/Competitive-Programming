# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AORB

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x, y = util.ints()
            a = 500 - x * 2 + 1000 - (y + x) * 4
            b = 1000 - y * 4 + 500 - (x + y) * 2
            print(max(a, b))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
