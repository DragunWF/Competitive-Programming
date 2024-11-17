# https://leetcode.com/problems/sum-of-unique-elements/description/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = set()
        duplicates = set()
        for num in nums:
            if not num in unique and not num in duplicates:
                unique.add(num)
            else:
                duplicates.add(num)
                unique.discard(num)
        return sum(unique)

