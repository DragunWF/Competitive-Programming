# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if matches[popped] != char:
                    return False
        return len(stack) == 0