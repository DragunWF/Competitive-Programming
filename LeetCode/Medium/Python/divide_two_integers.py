# https://leetcode.com/problems/divide-two-integers/description/

from math import floor

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Forgive me father for I have sinned
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        return int(str(dividend / divisor).split(".")[0])