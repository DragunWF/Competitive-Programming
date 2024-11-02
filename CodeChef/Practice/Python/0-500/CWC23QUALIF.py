# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CWC23QUALIF

class Solution:
    @staticmethod
    def solve():
        util = Solution
        x = util.int()
        print("yes" if x >= 12 else "no")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
