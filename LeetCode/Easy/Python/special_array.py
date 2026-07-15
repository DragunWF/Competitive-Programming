# https://leetcode.com/problems/special-array-i/description/

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 1):
            if (nums[i] % 2 == 0) == (nums[i + 1] % 2 == 0):
                return False
        return True
