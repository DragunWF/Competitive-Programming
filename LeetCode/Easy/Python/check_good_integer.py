# https://leetcode.com/problems/check-good-integer/

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        int_arr = [int(digit) for digit in str(n)]
        digit_sum = 0
        square_sum = 0
        for num in int_arr:
            digit_sum += num
            square_sum += num ** 2
        return square_sum - digit_sum >= 50
