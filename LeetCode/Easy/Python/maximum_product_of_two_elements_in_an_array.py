# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_copy = nums.copy()
        nums_copy.sort(reverse=True)
        return (nums_copy[0] - 1) * (nums_copy[1] - 1)
