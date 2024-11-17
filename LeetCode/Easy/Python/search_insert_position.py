# https://leetcode.com/problems/search-insert-position/description/?source=submission-noac

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return mid + 1 if target > nums[mid] else mid
 