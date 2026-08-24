# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

from typing import List
from itertools import product


class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]

        cartesian_product = list(product(["0", "1"], repeat=n))
        output = []
        for item in cartesian_product:
            binary_string = "".join(item)
            if self.isValidBinaryString(binary_string):
                output.append(binary_string)
        return output

    def isValidBinaryString(self, binary: str) -> bool:
        for i in range(len(binary)):
            if binary[i] == "0" and i + 1 != len(binary) and binary[i + 1] == "0":
                return False
        return True


def test() -> None:
    solution = Solution()
    print(solution.validStrings(2))
    print(solution.validStrings(3))


if __name__ == "__main__":
    test()
