# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FINDSHOES

class Solution:
    @staticmethod
    def solve():
        util = Solution
        T = util.num()
        for _ in range(T):
            n, m = util.ints()
            if m >= n:
                print(n)
            else:
                print(n * 2 - m)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
