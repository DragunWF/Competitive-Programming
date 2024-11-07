# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper() == word or word.lower() == word or word.title() == word