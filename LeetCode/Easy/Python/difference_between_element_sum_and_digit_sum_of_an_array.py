# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = 0
        digitSum = 0
        for num in nums:
            elementSum += num
            for digit in str(num):
                digitSum += int(digit)
        return abs(elementSum - digitSum)


def test() -> None:
    solution = Solution()
    # Expected: 9
    print(solution.differenceOfSum([1, 15, 6, 3]))


if __name__ == "__main__":
    test()
