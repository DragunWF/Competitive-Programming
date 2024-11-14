# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible_sum = 0
        non_divisible_sum = 0
        for i in range(1, n + 1):
            if i % m == 0:
                divisible_sum += i
            else:
                non_divisible_sum += i
        return non_divisible_sum - divisible_sum