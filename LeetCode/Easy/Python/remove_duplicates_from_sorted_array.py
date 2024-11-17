# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for num in nums:
            if not num in unique:
                unique.append(num)
        nums.clear()
        for num in unique:
            nums.append(num)