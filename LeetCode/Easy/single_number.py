# https://leetcode.com/problems/single-number/description/

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for key in counts:
            if counts[key] == 1:
                return key