# https://leetcode.com/problems/find-words-containing-character/description/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for i, word in enumerate(words):
            if x in word:
                output.append(i)
        return output