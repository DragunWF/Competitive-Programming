# https://leetcode.com/problems/subsets-ii/description/

from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        n = len(nums)
        for i in range(1, n + 1):
            subset_group = combinations(nums, i)
            for subset in subset_group:
                subset = sorted(list(subset))
                if not subset in subsets:
                    subsets.append(subset)
        return subsets