# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        for n in range(num1, num2 + 1):
            if n < 100:
                continue
            total_waviness += self.countWaviness(n)
        return total_waviness

    def countWaviness(self, num: int) -> int:
        count = 0
        str_num = str(num)
        for i in range(1, len(str_num) - 1):
            left_digit = int(str_num[i - 1])
            middle = int(str_num[i])
            right_digit = int(str_num[i + 1])
            if (middle > left_digit and middle > right_digit) or (middle < left_digit and middle < right_digit):
                count += 1
        return count


def test() -> None:
    # Expected: 3
    print(Solution().totalWaviness(120, 130))


if __name__ == "__main__":
    test()
