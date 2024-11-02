# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MOVIE2X

class Solution:
    @staticmethod
    def solve():
        util = Solution
        x, y = util.int_arr()
        print(x - y // 2)

    @staticmethod
    def int_arr():
        return map(int, input().split(" "))


if __name__ == "__main__":
    Solution.solve()
