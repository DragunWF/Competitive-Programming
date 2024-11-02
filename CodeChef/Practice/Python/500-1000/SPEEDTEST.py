# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SPEEDTEST

class Solution:
    @staticmethod
    def solve():
        util = Solution
        t = util.int()
        for _ in range(t):
            a, x, b, y = util.ints()
            alice_speed, bob_speed = a / x, b / y
            if alice_speed > bob_speed:
                print("Alice")
            elif alice_speed < bob_speed:
                print("Bob")
            else:
                print("Equal")

    @staticmethod
    def ints():
        return map(int, input().split())

    @staticmethod
    def int():
        return int(input())


if __name__ == "__main__":
    Solution.solve()
