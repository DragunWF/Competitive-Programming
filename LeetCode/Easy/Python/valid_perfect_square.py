# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        current_num = 1
        while True:
            square = current_num ** 2
            if square == num:
                return True
            if square > num:
                break
            current_num += 1
        return False
