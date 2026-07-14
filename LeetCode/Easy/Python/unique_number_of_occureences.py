# https://leetcode.com/problems/unique-number-of-occurrences/description/

from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        values = counter.values()
        return len(values) == len(set(values))
