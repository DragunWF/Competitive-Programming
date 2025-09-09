# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(self.digitSum(num) for num in nums)

    def digitSum(self, num: int) -> int:
        return sum([int(digit) for digit in str(num)])
