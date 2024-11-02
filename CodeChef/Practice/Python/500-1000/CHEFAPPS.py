# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFAPPS

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            s, x, y, z = util.ints()
            if s - (x + y) >= z:
                print(0)
            elif s - x >= z or s - y >= z:
                print(1)
            else:
                print(2)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
