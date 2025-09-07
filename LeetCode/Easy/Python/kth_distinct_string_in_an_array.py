# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/

from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        distinctElements = []
        for key in counter:
            if counter[key] == 1:
                distinctElements.append(key)
        return "" if k > len(distinctElements) else distinctElements[k - 1]


def test() -> None:
    solution = Solution()
    # Expected: a
    print(solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2))


if __name__ == "__main__":
    test()
