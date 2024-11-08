# https://leetcode.com/problems/regular-expression-matching/description/

import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.compile(f"^{p}$").match(s))
