# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DISCUS

class Solution:
    @staticmethod
    def solve():
        S = Solution
        T = int(input())
        for _ in range(T):
            a, b, c = S.int_arr()
            print(max(a, b, c))

    @staticmethod
    def int_arr():
        return map(int, input().split(" "))


if __name__ == "__main__":
    Solution.solve()
