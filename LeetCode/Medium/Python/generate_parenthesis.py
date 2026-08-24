# https://leetcode.com/problems/generate-parentheses/description/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        solution = []
        def backtrack(openCount, closeCount):
            if len(solution) == n * 2:
                answer.append("".join(solution))
                return
            if openCount < n:
                solution.append("(")
                backtrack(openCount + 1, closeCount)
                solution.pop()
            if openCount > closeCount:
                solution.append(")")
                backtrack(openCount, closeCount + 1)
                solution.pop()
        backtrack(0, 0)
        return answer