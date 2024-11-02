# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ERROR404

class Solution:
    @staticmethod
    def solve():
        util = Solution
        print("FOUND" if input() != "404" else "NOT FOUND")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
