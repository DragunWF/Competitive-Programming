# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WTRMIXING

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            a, b, x, y = util.ints()
            if x < y:
                print("YES" if a + x >= b else "NO")
            elif x > y:
                print("YES" if a - y <= b else "NO")
            else:
                print(0)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
