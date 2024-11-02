# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRANSFORM

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.num()
        states = ("small", "normal", "huge")
        for _ in range(t):
            x = util.num()
            current = 1 + x  # Normal index + x
            print(states[current % 3])

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
