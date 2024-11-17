# https://leetcode.com/contest/weekly-contest-424/problems/make-array-elements-equal-to-zero/description/

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        validSelections = 0
        for i, num in enumerate(nums):
            if num == 0:
                if self.is_valid(nums, i, "right"):
                    validSelections += 1
                if self.is_valid(nums, i, "left"):
                    validSelections += 1
        return validSelections

    def is_valid(self, nums: List[int], curr: int, direction: str) -> bool:
        left_sum = sum(nums[0:curr + 1])
        right_sum = sum(nums[curr: len(nums)])
        if direction == "right" and left_sum:
            left_sum -= 1
        else:
            right_sum -= 1
        if left_sum == right_sum:
            return True
        if direction == "right":
            left_sum += 1
        else:
            right_sum += 1
        return left_sum == right_sum


if __name__ == "__main__":
    # Test
    print(Solution().countValidSelections([16, 0, 0, 12, 5]))
