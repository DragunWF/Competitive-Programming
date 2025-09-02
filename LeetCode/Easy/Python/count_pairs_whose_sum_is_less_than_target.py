# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

from typing import List
from itertools import combinations


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = combinations(nums, 2)
        count = 0
        for pair in pairs:
            if sum(pair) < target:
                count += 1
        return count


def test() -> None:
    solution = Solution()
    # Expected: 3
    print(solution.countPairs([-1, 1, 2, 3, 1], 2))


if __name__ == "__main__":
    test()
