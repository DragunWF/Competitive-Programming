# https://leetcode.com/problems/reverse-degree-of-a-string/

from string import ascii_lowercase


class Solution:
    def reverseDegree(self, s: str) -> int:
        s = s.lower()
        letter_map = self.map_to_dict(ascii_lowercase)
        total = 0
        for i, char in enumerate(s):
            total += (i + 1) * letter_map[char]
        return total

    def map_to_dict(self, letters: str) -> dict:
        output = {}
        for i, letter in enumerate(reversed(letters)):
            output[letter] = i + 1
        return output


def test() -> None:
    solution = Solution()
    print(solution.map_to_dict(ascii_lowercase))
    print(solution.reverseDegree("abc"))  # 148


if __name__ == "__main__":
    test()
