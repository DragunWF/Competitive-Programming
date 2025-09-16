# https://leetcode.com/problems/create-target-array-in-the-given-order/

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        N = len(nums)
        target = [None for i in range(N)]
        for i in range(N):
            target.insert(index[i], nums[i])
        return [element for element in target if element is not None]
