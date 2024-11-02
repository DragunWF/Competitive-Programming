# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MAXTASTE

class Solution:
    @staticmethod
    def solve():
        util = Solution
        T = int(input())
        for _ in range(T):
            a, b, c, d = util.int_arr()
            print(max(a, b) + max(c, d))

    @staticmethod
    def int_arr():
        return map(int, input().split(" "))


if __name__ == "__main__":
    Solution.solve()
