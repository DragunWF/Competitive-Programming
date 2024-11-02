# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CYCLICQD

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            a, b, c, d = util.ints()
            if a + c == 180 and b + d == 180:
                print("YES")
            else:
                print("NO")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
