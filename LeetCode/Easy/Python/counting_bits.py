# https://leetcode.com/problems/counting-bits/description/

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            output.append(self.countZeros(i))
        return output

    def countZeros(self, n: int) -> int:
        count = 0
        for digit in bin(n)[2:]:
            if digit == "1":
                count += 1
        return count       