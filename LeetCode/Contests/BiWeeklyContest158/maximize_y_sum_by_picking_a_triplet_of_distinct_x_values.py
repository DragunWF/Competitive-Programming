# https://leetcode.com/contest/biweekly-contest-158/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/
# Solution Status - Solved

from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        if len(set(x)) < 3:
            return -1

        taken_values = set()
        max_i_value = self.getMaxSum(x, y, taken_values)
        max_j_value = self.getMaxSum(x, y, taken_values)
        max_k_value = self.getMaxSum(x, y, taken_values)

        return max_i_value + max_j_value + max_k_value

    def getMaxSum(self, x: List[int], y: List[int], taken_values: set) -> int:
        N = len(x)

        max_value = 0
        index_of_max_value = 0
        for i in range(N):
            if not x[i] in taken_values and y[i] > max_value:
                max_value = y[i]
                index_of_max_value = i

        taken_values.add(x[index_of_max_value])
        return max_value
