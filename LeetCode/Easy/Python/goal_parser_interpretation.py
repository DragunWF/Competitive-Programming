# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        output = ""
        for char in command:
            if char.isalpha():
                output += char
        return output


def test() -> None:
    solution = Solution()
    print(solution.interpret("G()(al)"))


if __name__ == "__main__":
    test()
