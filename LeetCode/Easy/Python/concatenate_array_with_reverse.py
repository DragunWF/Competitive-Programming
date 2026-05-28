# https://leetcode.com/problems/concatenate-array-with-reverse/description/

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return [*nums, *list(reversed(nums))]
