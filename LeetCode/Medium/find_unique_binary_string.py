# https://leetcode.com/problems/find-unique-binary-string/

from typing import List
from itertools import product


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for binary in product("01", repeat=n):
            joined_binary = "".join(binary)
            if not joined_binary in nums:
                return joined_binary


def test() -> None:
    solution = Solution()
    print(solution.findDifferentBinaryString(["01", "10"]))  # "11" or "00"


if __name__ == "__main__":
    test()
