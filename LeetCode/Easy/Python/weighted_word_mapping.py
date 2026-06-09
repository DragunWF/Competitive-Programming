# https://leetcode.com/problems/weighted-word-mapping/

from typing import List
from string import ascii_lowercase


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        output = []
        weight_map = self.mapWeights(weights)
        reversed_alphabets = ascii_lowercase[::-1]
        for word in words:
            total = 0
            for char in word:
                total += weight_map[char]
            output.append(reversed_alphabets[total % 26])
        return "".join(output)

    def mapWeights(self, weights: List[int]) -> str:
        mapped = {}
        for i, weight in enumerate(weights):
            mapped[ascii_lowercase[i]] = weight
        return mapped


def test() -> None:
    words = ["abcd", "def", "xyz"]
    weights = [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]
    # Expected: "rij"
    print(Solution().mapWordWeights(words, weights))


if __name__ == "__main__":
    test()
