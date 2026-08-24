# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    max_val = 2 ** 31
    min_val = -max_val

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if len(s) == 1:
            return int(s) if s.isdigit() else 0
        sign = ""
        if s[0] in ("+", "-"):
            if s[1] in ("+", "-"):
                return 0
            sign = s[0]
        first_num = self.get_first_num(s)
        
        try:
            print(f"{sign}{first_num}")
            value = int(f"{sign}{first_num}")
            if value >= Solution.max_val:
                return Solution.max_val - 1
            elif value < Solution.min_val:
                return Solution.min_val
            return value
        except ValueError:
            return 0
    
    def get_first_num(self, s: str) -> int:
        result = ""
        for char in s:
            if char.isdigit() or char == "-" or char == "+":
                if char.isdigit():
                    result += char
                elif result.isdigit():
                    break
            else:
                break
        return int(result) if result else 0
