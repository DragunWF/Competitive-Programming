# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/LASTLEVELS

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.num()
        for _ in range(t):
            x, y, z = util.ints()
            breaks = x / 3
            if breaks % 1 == 0:
                breaks -= 1
            breaks_time = max(0, int(breaks) * z)
            print(x * y + breaks_time)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
