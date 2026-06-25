# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/

from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        current_nums = nums.copy()
        averages = []
        while current_nums:
            max_num = max(current_nums)
            min_num = min(current_nums)
            averages.append((min_num + max_num) / 2)
            current_nums.pop(current_nums.index(max_num))
            current_nums.pop(current_nums.index(min_num))
        return min(averages)
