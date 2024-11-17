# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = self.sumDigits(num)
        return num
    
    def sumDigits(self, num: int) -> int:
        return sum(int(n) for n in str(num))