# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == len(set(nums)):
            return [nums]
        matrix = []
        for num in nums:
            changes = False
            for row in matrix:
                if not num in row:
                    row.append(num)
                    changes = True
                    break
            if not changes:
                matrix.append([])
                matrix[-1].append(num)
        return matrix