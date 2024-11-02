# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BLACKJACK

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            a, b = util.ints()
            num_needed = 21 - (a + b)
            print(num_needed if 1 <= num_needed <= 10 else -1)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
