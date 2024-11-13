# https://leetcode.com/problems/smallest-even-multiple/description/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(sum(nums[0:i + 1]))
        return output