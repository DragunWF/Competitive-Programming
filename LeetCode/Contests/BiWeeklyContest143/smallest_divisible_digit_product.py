# https://leetcode.com/contest/biweekly-contest-143/problems/smallest-divisible-digit-product-i/description/

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while self.digit_product(i) % t != 0:
            i += 1
        return i

    def digit_product(self, num: int) -> int:
        if num <= 9:
            return num
        str_num = str(num)
        product = int(str_num[0])
        for i in range(1, len(str_num)):
            product *= int(str_num[i])
        return product
