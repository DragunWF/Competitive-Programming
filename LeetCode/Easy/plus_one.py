# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(digit) for digit in digits)) + 1
        return [int(n) for n in str(num)]