# https://leetcode.com/problems/single-number-ii/description/

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        for key in count:
            if count[key] == 1:
                return key