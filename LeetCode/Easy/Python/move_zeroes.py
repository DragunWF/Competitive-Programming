# https://leetcode.com/submissions/detail/1463810054/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        non_zeroes = []
        for num in nums:
            if num == 0:
                zeroes.append(num)
            else:
                non_zeroes.append(num)
        nums.clear()
        for num in [*non_zeroes, *zeroes]:
            nums.append(num)