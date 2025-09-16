# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i, word in enumerate(words):
            words[i] = "".join(reversed([*word]))
        return " ".join(words)
