# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        VOWELS = "aeiou"

        vowel_count = {}
        consonant_count = {}
        for char in s:
            if char in VOWELS:
                self.mapCharToDict(vowel_count, char)
            else:
                self.mapCharToDict(consonant_count, char)

        max_vowel_count = max(vowel_count.values()) if vowel_count else 0
        max_consonant_count = max(consonant_count.values()) if consonant_count else 0
        return max_vowel_count + max_consonant_count

    def mapCharToDict(self, map: dict, char: str) -> None:
        if not char in map:
            map[char] = 1
        else:
            map[char] += 1


def test() -> None:
    solution = Solution()
    print(solution.maxFreqSum("successes"))  # 6


if __name__ == "__main__":
    test()
