# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_index = 0
            min_value = float("inf")
            for j, num in enumerate(nums):
                if num < min_value:
                    min_value = num
                    min_index = j
            nums[min_index] *= multiplier
        return nums


def test() -> None:
    solution = Solution()
    # Expected: [8,4,6,5,6]
    print(solution.getFinalState([2, 1, 3, 5, 6], 5, 2))


if __name__ == "__main__":
    test()
