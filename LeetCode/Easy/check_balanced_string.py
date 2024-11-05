# https://leetcode.com/problems/check-balanced-string/description/

class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = 0
        odd_sum = 0
        for i in range(len(num)):
            if i % 2 == 0:
                even_sum += int(num[i])
            else:
                odd_sum += int(num[i])
        return even_sum == odd_sum