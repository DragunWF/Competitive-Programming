# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(sum(nums[0:i + 1]))
        return output