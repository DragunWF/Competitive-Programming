# https://leetcode.com/problems/combinations/description/

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums) + 1):
            subsets = list(combinations(nums, i))
            for subset in subsets:
                output.append(subset)
        return output