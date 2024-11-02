# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/OFFBY1

class Solution:
    @staticmethod
    def solve():
        util = Solution
        a, b = util.ints()
        print(f"{a + b}1")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
