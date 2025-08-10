# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/

from typing import List


class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        n = len(a)
        output = []
        seen_a, seen_b = set(), set()
        for i in range(n):
            seen_a.add(a[i])
            seen_b.add(b[i])
            output.append(self.countCommon(seen_a, seen_b))
        return output

    def countCommon(self, a: set, b: set) -> int:
        return len(a & b)


def test() -> None:
    solution = Solution()
    print(solution.findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]))


if __name__ == "__main__":
    test()
