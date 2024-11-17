# https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [*nums, *nums]
