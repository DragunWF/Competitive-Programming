# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFBOTTLE

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.num()
        for _ in range(t):
            n, x, k = util.ints()
            print(min((n * x) // x, k // x))

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
