# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOUBLERENT

class Solution:
    @staticmethod
    def solve():
        util = Solution
        x = util.int()
        print(x * 2)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
