# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique = []
        for num in nums:
            if not nums in unique:
                unique.append(num)
            else:
                return False
        return True
        