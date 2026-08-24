# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        output = [-1, -1]
        for i, num in enumerate(nums):
            if num == target and output[0] == -1:
                output[0] = i
            elif num != target and output[0] != -1:
                output[1] = i - 1
            if output[0] != -1 and output[1] != -1:
                break
            if i == len(nums) - 1 and output[0] != -1:
                output[1] = i
        return output