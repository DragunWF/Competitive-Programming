# https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum = sum(n for n in nums if n <= 9)
        double_digit_sum = sum(n for n in nums if n > 9)
        return single_digit_sum > double_digit_sum or double_digit_sum > single_digit_sum