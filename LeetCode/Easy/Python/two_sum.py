# https://leetcode.com/problems/two-sum/submissions/1443627464/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
