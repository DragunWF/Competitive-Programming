# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counter = self.createCounter(nums)
        total = 0
        for num in counter:
            if counter[num] % k == 0:
                total += num * counter[num]
        return total

    def createCounter(self, nums: List[int]) -> dict:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        return counter


def test() -> None:
    # Expected: 16
    print(Solution().sumDivisibleByK([1, 2, 2, 3, 3, 3, 3, 4], 2))


if __name__ == "__main__":
    test()
