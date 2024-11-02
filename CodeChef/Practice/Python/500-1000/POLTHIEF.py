# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/POLTHIEF

class Solution:
    @staticmethod
    def solve():
        util = Solution
        T = int(input())
        for _ in range(T):
            x, y = util.int_arr()
            print(abs(x - y))

    @staticmethod
    def int_arr():
        return map(int, input().split(" "))


if __name__ == "__main__":
    Solution.solve()
