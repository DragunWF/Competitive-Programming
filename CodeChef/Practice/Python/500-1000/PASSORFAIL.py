# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/PASSORFAIL

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            n, x, p = util.ints()
            print("PASS" if x * 3 - (n - x) >= p else "FAIL")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
