# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        padded_zero_count = 32 - len(binary)
        binary_32_bit = "0" * padded_zero_count + binary
        return int(binary_32_bit[::-1], 2)


def test() -> None:
    solution = Solution()
    print(solution.reverseBits(43261596))


if __name__ == "__main__":
    test()
