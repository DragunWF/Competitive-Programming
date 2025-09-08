# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


def test() -> None:
    solution = Solution()
    # ada
    print(solution.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))


if __name__ == "__main__":
    test()
