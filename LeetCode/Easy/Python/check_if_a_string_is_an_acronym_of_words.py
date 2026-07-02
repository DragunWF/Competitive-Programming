# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        target_acronym = ""
        for word in words:
            target_acronym += word[0]
        return s == target_acronym
