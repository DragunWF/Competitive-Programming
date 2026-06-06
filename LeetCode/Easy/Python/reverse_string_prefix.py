# https://leetcode.com/problems/reverse-string-prefix/description/

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return f"{s[:k][::-1]}{s[k:]}"
