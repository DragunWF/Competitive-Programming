# https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))
