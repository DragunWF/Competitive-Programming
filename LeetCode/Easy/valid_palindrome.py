# https://leetcode.com/problems/valid-palindrome/description/

from string import ascii_lowercase, digits


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ascii_lowercase + digits
        output = ""
        for char in s.lower():
            if char in alphanumeric:
                output += char
        return output == output[::-1]
