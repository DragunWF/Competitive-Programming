# https://leetcode.com/problems/permutation-sequence/description/

from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [*range(1, n + 1)]
        all_permutations = list(permutations(nums))
        return "".join(str(i) for i in all_permutations[k - 1])
        