# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AUDIBLE

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            x = util.int()
            print("YES" if 67 <= x <= 45000 else "NO")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
