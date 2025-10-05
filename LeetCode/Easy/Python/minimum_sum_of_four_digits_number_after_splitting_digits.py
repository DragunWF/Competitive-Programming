# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted([int(digit) for digit in str(num)])
        return int(f"{digits[0]}{digits[2]}") + int(f"{digits[1]}{digits[3]}")


def test() -> None:
    solution = Solution()
    print(solution.minimumSum(2932))  # 52
    print(solution.minimumSum(4009))  # 13


if __name__ == "__main__":
    test()
