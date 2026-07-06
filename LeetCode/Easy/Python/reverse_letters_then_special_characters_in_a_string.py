# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/description/

class Solution:
    def reverseByType(self, s: str) -> str:
        SPECIAL, NORMAL = "special", "normal"

        type_per_pos = []
        normal_chars = []
        special_chars = []
        for char in s:
            if char.isalpha():
                type_per_pos.append(NORMAL)
                normal_chars.append(char)
            else:
                type_per_pos.append(SPECIAL)
                special_chars.append(char)

        normal_chars.reverse()
        special_chars.reverse()

        output = []
        normal_char_index = 0
        special_char_index = 0
        for i in range(len(s)):
            if type_per_pos[i] == NORMAL:
                output.append(normal_chars[normal_char_index])
                normal_char_index += 1
            elif type_per_pos[i] == SPECIAL:
                output.append(special_chars[special_char_index])
                special_char_index += 1
        return "".join(output)


def test() -> None:
    # Expected: "(fad@cb#e)"
    print(Solution().reverseByType(")ebc#da@f("))


if __name__ == "__main__":
    test()
