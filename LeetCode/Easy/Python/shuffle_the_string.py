# https://leetcode.com/problems/shuffle-string/

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [None for i in range(len(s))]
        for char, index in zip(s, indices):
            output[index] = char
        return "".join(output)


def test() -> None:
    solution = Solution()
    print(solution.restoreString("codeleet", [
          4, 5, 6, 7, 0, 2, 1, 3]))  # LeetCode


if __name__ == "__main__":
    test()
