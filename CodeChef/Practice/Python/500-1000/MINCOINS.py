# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINCOINS

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x = util.int()
            if x % 5 != 0:
                print(-1)
            elif x % 10 == 0:
                print(x // 10)
            else:
                print(x // 10 + 1)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
