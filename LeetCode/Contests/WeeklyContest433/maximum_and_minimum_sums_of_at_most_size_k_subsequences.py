# https://leetcode.com/contest/weekly-contest-433/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/description/

# Memory Limit Exceeded

from typing import List
from itertools import combinations


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        if k == 1:
            return (sum(nums) * 2) % (10 ** 9 + 7)

        n = len(nums)
        k = min(k, n)
        total_sum = 0

        for i in range(k):
            subsequences = list(combinations(nums, i + 1))
            for subsequence in subsequences:
                total_sum += min(subsequence) + max(subsequence)

        return total_sum % (10 ** 9 + 7)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minMaxSums([1, 2, 3], 2))  # 24
    print(solution.minMaxSums([5, 0, 6], 1))  # 22
    print(solution.minMaxSums([1, 1, 1], 2))  # 12
