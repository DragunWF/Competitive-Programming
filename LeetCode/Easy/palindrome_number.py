# https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 <= x <= 9:
            return True
        str_num = [*str(x)]
        str_num.reverse()
        return "".join(str_num) == str(x)
        