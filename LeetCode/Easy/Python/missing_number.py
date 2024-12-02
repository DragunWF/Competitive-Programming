# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([n for n in range(len(nums) + 1)]) - sum(nums)