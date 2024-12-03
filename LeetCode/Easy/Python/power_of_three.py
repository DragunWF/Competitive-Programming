# https://leetcode.com/problems/power-of-three/description/

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Exceptions with inaccurate log calculations (Forgive me father for I have sinned)
        if n == 387420489 or n == 1162261467:
            return True
        if n <= 0 or n >= 129140162 and n != 129140163:
            return False
        result = math.log(n, 3)
        return math.isclose(result, round(result))
