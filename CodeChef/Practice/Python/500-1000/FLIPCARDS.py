# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLIPCARDS

class Solution:
    @staticmethod
    def solve():
        util = Solution
        T = util.num()
        for _ in range(T):
            n, x = util.ints()
            print(min(n - x, x))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
