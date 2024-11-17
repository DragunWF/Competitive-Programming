# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        values = {}
        seen_words = set()
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        try:
            for i in range(len(pattern)):
                if not words[i] in seen_words and not pattern[i] in values:
                    values[pattern[i]] = words[i]
                    seen_words.add(words[i])
                else:
                    if (words[i] in seen_words and values[pattern[i]] != words[i] or 
                        not words[i] in seen_words and pattern[i] in values):
                        return False
        except:
            return False
        return True