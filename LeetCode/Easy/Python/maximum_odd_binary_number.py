# https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_bits_count = 0
        zero_bits_count = 0
        for digit in s:
            if digit == "1":
                one_bits_count += 1
            else:
                zero_bits_count += 1

        output = ""
        output += (one_bits_count - 1) * "1"
        output += zero_bits_count * "0"
        return f"{output}1"


def test() -> None:
    solution = Solution()
    print(solution.maximumOddBinaryNumber("010"))  # 001
    print(solution.maximumOddBinaryNumber("0101"))  # 1001


if __name__ == "__main__":
    test()
