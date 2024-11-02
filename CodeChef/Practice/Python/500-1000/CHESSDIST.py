# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHESSDIST

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x1, y1, x2, y2 = util.ints()
            print(max(abs(x1 - x2), abs(y1 - y2)))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
