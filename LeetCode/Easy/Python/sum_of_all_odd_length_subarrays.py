# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr)):
                if j + i > len(arr):
                    break
                total += sum(arr[j:j + i])
        return total


def test() -> None:
    # Expected: 58
    print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))


if __name__ == "__main__":
    test()
