# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW017

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            a, b, c = util.ints()
            print(sorted([a, b, c])[1])

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
