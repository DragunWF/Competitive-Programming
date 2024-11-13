# https://leetcode.com/problems/smallest-even-multiple/description/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for i in range(len(s)):
            total += abs(i - t.index(s[i]))
        return total
