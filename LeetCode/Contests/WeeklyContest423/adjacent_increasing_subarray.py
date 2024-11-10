# https://leetcode.com/contest/weekly-contest-423/problems/adjacent-increasing-subarrays-detection-i/

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            current = nums[i:i + k]
            adjacent = nums[i + k:i + k * 2]
            if len(adjacent) != k:
                return False
            if len(set(current)) != len(current) or len(set(adjacent)) != len(adjacent):
                continue
            if sorted(current) == current and sorted(adjacent) == adjacent:
                return True
        return False
