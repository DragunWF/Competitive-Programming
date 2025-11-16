# https://leetcode.com/problems/valid-parentheses/submissions/1831252700/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_matches = {"}": "{", "]": "[", ")": "("}
        opening = closing_matches.values()
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing_matches:
                if not stack:
                    return False
                opening_char = stack.pop()
                if closing_matches[char] != opening_char:
                    return False
        return len(stack) == 0