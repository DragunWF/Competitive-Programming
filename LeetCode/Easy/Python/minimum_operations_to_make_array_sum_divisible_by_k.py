# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        operations_needed = 0
        while total % k != 0:
            total -= 1
            operations_needed += 1
        return operations_needed
