# https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        goodPairsCount = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    goodPairsCount += 1
        return goodPairsCount


def test() -> None:
    solution = Solution()
    # 5
    print(solution.numberOfPairs([1, 3, 4], [1, 3, 4], 1))


if __name__ == "__main__":
    test()
