# https://leetcode.com/problems/sort-colors/description/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Must be solved without using in-built functions so here it is
        for i in range(len(nums)):
            is_sorted = True
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    is_sorted = False
            if is_sorted:
                break