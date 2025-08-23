# https://leetcode.com/problems/find-center-of-star-graph/description/

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = {}
        for edge in edges:
            for num in edge:
                if not num in count:
                    count[num] = 1
                else:
                    count[num] += 1
        return self.getMaxCountKey(count)

    def getMaxCountKey(self, count: dict) -> int:
        max_key = None
        max_value = float("-inf")
        for key in count:
            if count[key] > max_value:
                max_key = key
                max_value = count[key]
        return max_key


def test() -> None:
    solution = Solution()
    # Expected: 2
    print(solution.findCenter([[1, 2], [2, 3], [4, 2]]))


if __name__ == "__main__":
    test()
