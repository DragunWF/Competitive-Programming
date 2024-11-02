# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DECINC

class Solution:
    @staticmethod
    def solve():
        util = Solution
        n = util.int()
        print(n + 1 if n % 4 == 0 else n - 1)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()

