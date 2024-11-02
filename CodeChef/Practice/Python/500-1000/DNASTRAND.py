# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DNASTRAND

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.num()
        complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
        for _ in range(t):
            n = util.num()
            s = input()
            for i in range(n):
                print(complements[s[i]], end="")
            print()

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def num():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
