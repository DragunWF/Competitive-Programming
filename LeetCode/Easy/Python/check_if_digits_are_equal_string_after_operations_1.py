# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        current_str = s
        while len(current_str) != 2:
            new_str = []
            for i in range(1, len(current_str)):
                current_num = int(current_str[i])
                prev_num = int(current_str[i - 1])
                new_str.append(str((current_num + prev_num) % 10))
            current_str = "".join(new_str)
        return current_str[0] == current_str[1]


def test() -> None:
    # Expected: true
    print(Solution().hasSameDigits("3902"))


if __name__ == "__main__":
    test()
