# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0
        for i in range(N):
            for j in range(i, N):
                if i == j:
                    continue
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count


def test() -> None:
    solution = Solution()
    # Expected: 2
    print(solution.countPairs([3, 1, 2, 2, 2, 1, 3], 2))


if __name__ == "__main__":
    test()
