# https://leetcode.com/problems/truncate-sentence/description/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        return " ".join(words[:k])
