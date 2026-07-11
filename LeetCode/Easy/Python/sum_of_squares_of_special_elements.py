# https://leetcode.com/problems/sum-of-squares-of-special-elements/description/

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        for i, num in enumerate(nums):
            if len(nums) % (i + 1) == 0:
                total += num ** 2
        return total
