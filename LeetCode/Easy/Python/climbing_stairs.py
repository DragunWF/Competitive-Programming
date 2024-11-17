# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        seq = [1, 2]
        if n <= len(seq):
            return seq[n - 1]
        for i in range(len(seq) - 1, n - 1):
            seq.append(seq[i] + seq[i - 1])
        return seq[-1]
    