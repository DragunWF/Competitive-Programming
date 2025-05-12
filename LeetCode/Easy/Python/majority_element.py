# https://leetcode.com/problems/majority-element/

from types import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element, max_count = None, 0
        counter = Counter(nums)
        for key in counter.keys():
            if counter[key] > max_count:
                majority_element = key
                max_count = counter[key]
        return majority_element
