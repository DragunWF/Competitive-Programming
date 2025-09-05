# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


def test() -> None:
    solution = Solution()
    print(solution.prefixCount(
        ["pay", "attention", "practice", "attend"], "at"))


if __name__ == "__main__":
    test()
