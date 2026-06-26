# https://leetcode.com/problems/find-missing-elements/

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = []
        for i in range(1, len(nums)):
            expected = nums[i] - 1
            if nums[i - 1] != expected:
                current_missing_num = expected
                while current_missing_num != nums[i - 1]:
                    missing.append(current_missing_num)
                    current_missing_num -= 1
        missing.sort()
        return missing
