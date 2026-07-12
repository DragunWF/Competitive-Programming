# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        for num in set(nums1):
            if not num in nums2:
                answer[0].append(num)
        for num in set(nums2):
            if not num in nums1:
                answer[1].append(num)
        return answer


def test() -> None:
    solution = Solution()

    # Expected: [[1,3],[4,6]]
    print(solution.findDifference([1, 2, 3], [2, 4, 6]))

    # Expected: [[3],[]]
    print(solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))


if __name__ == "__main__":
    test()
