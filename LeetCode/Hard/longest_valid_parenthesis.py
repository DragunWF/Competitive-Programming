# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid = []
        for char in s:
            if char == "(":
                valid.append(0)
            else:
                for i in range(1, len(valid) + 1):
                    if valid[-i] == 0:
                        valid[-i] = 1
                        break
                else:
                    valid.append(-1)
        return self.longest_consecutive(valid)
    
    def longest_consecutive(self, values: List[int]) -> int:
        longest = 0
        current = 0
        for num in values:
            if num == 1:
                current += 1
            else:
                if current > longest:
                    longest = current
                current = 0
        return max(longest * 2, current * 2)