# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse = s[::-1]
        s.clear()
        for char in reverse:
            s.append(char)