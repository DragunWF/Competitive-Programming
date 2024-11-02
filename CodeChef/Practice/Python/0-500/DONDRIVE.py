# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DONDRIVE

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            n, x = util.ints()
            print(n - x)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
