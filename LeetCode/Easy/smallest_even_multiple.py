# https://leetcode.com/problems/smallest-even-multiple/description/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1, 151):
            multiple = n * i
            if multiple % 2 == 0:
                return multiple