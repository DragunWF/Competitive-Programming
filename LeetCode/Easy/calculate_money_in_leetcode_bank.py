# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        previous_monday = 0
        cash_deposit = previous_monday
        for i in range(n):
            cash_deposit += 1
            total += cash_deposit
            if (i + 1) % 7 == 0:
                previous_monday += 1
                cash_deposit = previous_monday
        return total