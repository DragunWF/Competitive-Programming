# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFEREN

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            n, a, b = util.ints()
            even_episodes = n // 2
            print(even_episodes * a + (n - even_episodes) * b)

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()

