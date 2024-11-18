# https://leetcode.com/problems/defuse-the-bomb/description/?envType=daily-question&envId=2024-11-18

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        output = []
        n = len(code)
        for i in range(n):
            total = 0
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    total += code[j % n]
            elif k < 0:
                for j in range(i - 1, i + k - 1, -1):
                    total += code[j % n]
            output.append(total)
        return output
    