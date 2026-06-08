# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i, num in enumerate(nums):
            count = 0
            for j, compare_num in enumerate(nums):
                if i != j and compare_num < num:
                    count += 1
            output.append(count)
        return output
