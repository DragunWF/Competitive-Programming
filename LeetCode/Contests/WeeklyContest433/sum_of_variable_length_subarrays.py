# https://leetcode.com/contest/weekly-contest-433/problems/sum-of-variable-length-subarrays/description/

from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            start = max(0, i - nums[i])
            total += sum(nums[start:i + 1])
        return total
