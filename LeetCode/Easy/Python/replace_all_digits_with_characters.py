# https://leetcode.com/problems/replace-all-digits-with-characters/

from string import ascii_lowercase, ascii_uppercase


class Solution:
    def replaceDigits(self, s: str) -> str:
        output = []
        for i, char in enumerate(s):
            if char.isalpha():
                output.append(char)
                continue
            alpha_char = s[i - 1]
            output.append(self.shift(alpha_char, int(char)))
        return "".join(output)

    def shift(self, char: str, number: int) -> str:
        if char.isupper():
            index = ascii_uppercase.index(char)
            return ascii_uppercase[index + number]
        index = ascii_lowercase.index(char)
        return ascii_lowercase[index + number]


def test() -> None:
    # Expected: "abcdef"
    print(Solution().replaceDigits("a1c1e1"))

    # Expected: "abbdcfdhe"
    print(Solution().replaceDigits("a1b2c3d4e"))


if __name__ == "__main__":
    test()
