# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CLEARDAY

class Solution:
    @staticmethod
    def solve():
        util = Solution
        x, y = util.ints()
        print(7 - (x + y))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
