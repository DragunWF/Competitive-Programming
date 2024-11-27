# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        binary = "".join(str(num) for num in nums)
        return max(len(consecutive) for consecutive in binary.split("0"))