# https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            digit_group = ""
            groups = []
            for i, digit in enumerate(s):
                digit_group += digit
                if (i + 1) % k == 0:
                    groups.append(digit_group)
                    digit_group = ""
            if digit_group:
                groups.append(digit_group)
            s = "".join(str(self.sumDigits(group)) for group in groups)
        return s
    
    def sumDigits(self, s: str) -> int:
        total = 0
        for digit in s:
            total += int(digit)
        return total
        