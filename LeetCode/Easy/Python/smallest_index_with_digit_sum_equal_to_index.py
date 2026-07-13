# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/

from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digit_sum = sum(int(char) for char in str(num))
            if digit_sum == i:
                return i
        return -1
