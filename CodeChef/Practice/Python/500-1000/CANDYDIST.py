# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CANDYDIST

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.num()
        for _ in range(t):
            n, m = util.ints()
            print("yes" if (n / m) % 2 == 0 else "no")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
