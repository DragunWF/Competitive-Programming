# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    max_val = 2 ** 31 - 1
    min_val = -(abs(max_val) + 1)

    def reverse(self, x: int) -> int:
        char_arr = None
        if x < 0:
            char_arr = [*str(x)[1:]]
        else:
            char_arr = [*str(x)]
        char_arr.reverse()
        reversed_num = int("".join(char_arr))
        if x < 0:
            reversed_num = -reversed_num
        return reversed_num if Solution.min_val <= reversed_num <= Solution.max_val else 0
