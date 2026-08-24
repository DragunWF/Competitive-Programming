# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            unique = set()
            for j in range(i, len(s)):
                if not s[j] in unique:
                    unique.add(s[j])
                else:
                    break
            if len(unique) > max_len:
                max_len = len(unique)
        return max_len