# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/IPLTRSH

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            n, m = util.ints()
            print(max(0, n - m))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
