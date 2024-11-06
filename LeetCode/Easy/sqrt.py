# https://leetcode.com/problems/sqrtx/submissions/1444618027/

from math import sqrt, floor

class Solution:
    def mySqrt(self, x: int) -> int:
        return floor(sqrt(x))