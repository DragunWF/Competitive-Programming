# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        seen_vowels = []
        indexes = []
        s = [*s]
        for i, char in enumerate(s):
            if char in vowels:
                seen_vowels.append(char)
                indexes.append(i)
        indexes.reverse()
        for i in range(len(indexes)):
            s[indexes[i]] = seen_vowels[i]
        return "".join(s)
