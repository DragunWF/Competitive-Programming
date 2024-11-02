# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TOP10

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x = util.int()
            print("YES" if x <= 10 else "NO")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
