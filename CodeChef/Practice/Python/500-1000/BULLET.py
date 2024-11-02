# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BULLET

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.num()
        for _ in range(t):
            x, y, z = util.ints()
            result = z - y / x
            print(int(result) if result >= 0 else 0)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
