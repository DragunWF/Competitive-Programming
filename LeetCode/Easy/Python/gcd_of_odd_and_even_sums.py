# https://leetcode.com/problems/gcd-of-odd-and-even-sums/

from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = 0
        even_sum = 0
        current_odd_num = 1
        current_even_num = 2
        for i in range(n):
            odd_sum += current_odd_num
            even_sum += current_even_num
            current_even_num += 2
            current_odd_num += 2
        return gcd(odd_sum, even_sum)


def test() -> None:
    # Expected: 4
    print(Solution().gcdOfOddEvenSums(4))


if __name__ == "__main__":
    test()
