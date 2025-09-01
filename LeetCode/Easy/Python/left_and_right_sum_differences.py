# https://leetcode.com/problems/left-and-right-sum-differences/

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        output = []
        leftSum = []
        rightSum = []
        for i in range(len(nums)):
            leftSum.append(self.getLeftSum(i, nums))
            rightSum.append(self.getRightSum(i, nums))
        for i in range(len(nums)):
            output.append(abs(leftSum[i] - rightSum[i]))
        return output

    def getLeftSum(self, currentIndex: int, nums: List[int]) -> int:
        total = 0
        for i in range(currentIndex - 1, -1, -1):
            total += nums[i]
        return total

    def getRightSum(self, currentIndex: int, nums: List[int]) -> int:
        total = 0
        for i in range(currentIndex + 1, len(nums)):
            total += nums[i]
        return total


def test() -> None:
    solution = Solution()
    print(solution.leftRightDifference([10, 4, 8, 3]))  # [15,1,11,22]


if __name__ == "__main__":
    test()
