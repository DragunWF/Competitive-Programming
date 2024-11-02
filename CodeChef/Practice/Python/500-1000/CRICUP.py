# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CRICUP

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x, y, d = util.ints()
            print("YES" if abs(x - y) <= d else "NO")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()

