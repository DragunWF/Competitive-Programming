# https://leetcode.com/problems/compute-alternating-sum/description/

from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even_sum, odd_sum = 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
        return even_sum - odd_sum
