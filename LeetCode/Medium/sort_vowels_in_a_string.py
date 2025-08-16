# https://leetcode.com/problems/sort-vowels-in-a-string/description/

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        output = []
        seen_vowels = []
        for char in s:
            if char in vowels:
                output.append("_")
                seen_vowels.append(char)
            else:
                output.append(char)
        seen_vowels.sort()

        seen_vowels_index = 0
        for i in range(len(s)):
            if output[i] == "_":
                output[i] = seen_vowels[seen_vowels_index]
                seen_vowels_index += 1

        return "".join(output)


def test() -> None:
    solution = Solution()
    print(solution.sortVowels("lEetcOde"))  # "lEOtcede"


if __name__ == "__main__":
    test()
