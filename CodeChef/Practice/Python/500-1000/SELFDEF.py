# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SELFDEF

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            input()
            ages = util.ints()
            eligible = 0
            for age in ages:
                if 10 <= age <= 60:
                    eligible += 1
            print(eligible)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
