# https://leetcode.com/problems/find-triangular-sum-of-an-array/

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        current_nums = nums.copy()
        summed_nums = []
        while len(current_nums) > 1:
            for i in range(len(current_nums) - 1):
                summed_nums.append((current_nums[i] + current_nums[i + 1]) % 10)
            current_nums = summed_nums.copy()
            summed_nums.clear()
        return current_nums[0]
