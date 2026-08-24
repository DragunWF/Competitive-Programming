# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        unique = set()
        duplicates = set()
        for num in nums:
            if not num in unique:
                unique.add(num)
            else:
                duplicates.add(num)
        return list(duplicates)