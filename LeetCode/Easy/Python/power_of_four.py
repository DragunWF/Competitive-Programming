# https://leetcode.com/problems/power-of-four/description/

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4) % 1 == 0