# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WTRMIXING

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            a, b, x, y = util.ints()
            if a < b:
                print("YES" if a + x >= b else "NO")
            elif a > b:
                print("YES" if a - y <= b else "NO")
            else:
                print("YES")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
