# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            sub_str = ""
            for j in range(i, min(i + len(needle), len(haystack))):
                sub_str += haystack[j]
            if sub_str == needle:
                return i
        return -1