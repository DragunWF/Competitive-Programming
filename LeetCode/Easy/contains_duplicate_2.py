# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            other = min(i + k, n - 1)
            subtractions = 0
            while i != other and subtractions <= 15:
                if nums[i] == nums[other]:
                    return True
                subtractions += 1
                other -= 1
        return False