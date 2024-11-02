# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DETSCORE

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x, n = util.ints()
            print((x // 10) * n)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
