# https://leetcode.com/problems/valid-number/description/

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if "inf" in s or "Infinity" in s or "nan" in s:
                return False
            if "e" in s or "E" in s:
                num = s.lower().split("e")
                if len(num) > 2 or "." in num[1]:
                    return False
                float(num[0])
                float(num[1])
            else:
                float(s)
            return True
        except:
            return False