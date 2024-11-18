# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        digit_sum = self.getDigitSum(n)
        while digit_sum > 9:
            digit_sum = self.getDigitSum(digit_sum)
        return digit_sum == 1 or digit_sum == 7
    
    def getDigitSum(self, n: int) -> int:
        return sum([int(i) ** 2 for i in str(n)])
        