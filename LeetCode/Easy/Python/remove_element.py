# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = []
        for num in nums:
            if num != val:
                removed.append(num)
        nums.clear()

        for num in removed:
            nums.append(num)