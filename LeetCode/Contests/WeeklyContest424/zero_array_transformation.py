# https://leetcode.com/contest/weekly-contest-424/problems/zero-array-transformation-i/description/

import numpy as np

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr = np.array(nums)
        for query in queries:
            arr[query[0]:query[1] + 1] -= 1
        return all(n <= 0 for n in arr)