# https://leetcode.com/problems/count-digit-appearances/

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        total = 0
        digit = str(digit)
        for num in nums:
            total += [*str(num)].count(digit)
        return total
