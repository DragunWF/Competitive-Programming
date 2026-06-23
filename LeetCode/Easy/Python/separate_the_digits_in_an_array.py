# https://leetcode.com/problems/separate-the-digits-in-an-array/description/

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digits = []
        for num in nums:
            separated_digits = [int(char) for char in str(num)]
            for digit in separated_digits:
                digits.append(digit)
        return digits
