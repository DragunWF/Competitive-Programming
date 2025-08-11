# https://leetcode.com/problems/reverse-prefix-of-word/description/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = []
        end_prefix_index = None
        for i, letter in enumerate(word):
            prefix.append(letter)
            if letter == ch:
                end_prefix_index = i
                break
        if end_prefix_index is None:
            return word
        return "".join(reversed(prefix)) + word[end_prefix_index + 1::]


def test() -> None:
    solution = Solution()
    print(solution.reversePrefix("abcdefd", "d"))  # "dcbaefd"


if __name__ == "__main__":
    test()
