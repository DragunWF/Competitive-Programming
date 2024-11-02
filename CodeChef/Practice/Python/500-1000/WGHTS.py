# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WGHTS

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            w, x, y, z = util.ints()
            r = (x, y, z, x + y, x + z, y + z, x + y + z)
            print("YES" if w in r else "NO")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
