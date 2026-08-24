# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            sub_str = ""
            for j in range(i, len(s)):
                sub_str += s[j]
                if sub_str == sub_str[::-1] and len(sub_str) > len(longest):
                    longest = sub_str
        return longest
