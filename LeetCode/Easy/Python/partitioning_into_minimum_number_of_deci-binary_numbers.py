# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(num) for num in n)
