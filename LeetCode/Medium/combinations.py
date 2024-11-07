# https://leetcode.com/problems/combinations/description/

from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        values = [i for i in range(1, n + 1)]
        return list(combinations(values, k))