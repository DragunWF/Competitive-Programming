# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            if num % 3 == 0:
                continue
            operations += 1
        return operations