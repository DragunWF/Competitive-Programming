# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        word1_index = 0
        word2_index = 0
        for i in range(max(len(word1), len(word2))):
            if word1_index < len(word1):
                output.append(word1[word1_index])
                word1_index += 1
            if word2_index < len(word2):
                output.append(word2[word2_index])
                word2_index += 1
        return "".join(output)
