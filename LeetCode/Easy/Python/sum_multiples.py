# https://leetcode.com/problems/sum-multiples/

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        return total


def test() -> None:
    solution = Solution()
    print(solution.sumOfMultiples(7))  # 21


if __name__ == "__main__":
    test()
