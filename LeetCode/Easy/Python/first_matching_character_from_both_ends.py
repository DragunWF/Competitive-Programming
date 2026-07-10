# https://leetcode.com/problems/first-matching-character-from-both-ends/

class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        offset = 0
        for i in range(len(s)):
            if s[i] == s[-(i + 1)]:
                break
            offset += 1
        else:
            return -1
        return offset
