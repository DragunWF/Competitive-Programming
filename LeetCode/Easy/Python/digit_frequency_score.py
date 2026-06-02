# https://leetcode.com/problems/digit-frequency-score/description/

from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        total = 0
        counter = Counter(str(n))
        for digit in counter:
            total += counter[digit] * int(digit)
        return total
