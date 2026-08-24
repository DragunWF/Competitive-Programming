# https://leetcode.com/problems/find-and-replace-pattern/description/

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        letterBijection = self.standardizeStr(pattern)
        n = len(pattern)
        for word in words:
            if n == len(word) and self.standardizeStr(word) == letterBijection:
                output.append(word)
        return output

    def standardizeStr(self, word: str) -> List[int]:
        letterMap = {}
        standardizedValue = []
        for char in word:
            if char in letterMap:
                standardizedValue.append(letterMap[char])
            else:
                letterMap[char] = hex(len(letterMap))
                standardizedValue.append(letterMap[char])
        return "".join(standardizedValue)


def test() -> None:
    solution = Solution()
    # ["mee","aqq"]
    print(solution.findAndReplacePattern(
        ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")
    )

    # []
    print(solution.findAndReplacePattern(["abcdefghijkba"], "qwertyuiopwqa"))


if __name__ == "__main__":
    test()
