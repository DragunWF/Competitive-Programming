# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BATH

class Solution:
    @staticmethod
    def solve():
        util = Solution
        T = util.num()
        for _ in range(T):
            x, y = util.ints()
            print(x // (y * 2))


    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
