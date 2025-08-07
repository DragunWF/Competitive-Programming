# https://leetcode.com/problems/shuffle-the-array/description/

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[n + i])
        return output


def test() -> None:
    solution = Solution()
    print(solution.shuffle([1, 1, 2, 2], 2))


if __name__ == "__main__":
    test()
