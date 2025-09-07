# https://leetcode.com/problems/clear-digits/

class Solution:
    def clearDigits(self, s: str) -> str:
        output = s
        while self.hasDigit(output):
            outputIteration = ""
            digitIndex = None
            letterIndex = None
            for i in range(len(output) - 1, -1, -1):
                if output[i].isdigit() and digitIndex is None:
                    digitIndex = i
                elif output[i].isalpha() and not digitIndex is None:
                    letterIndex = i
                if letterIndex and digitIndex:
                    break
            for i in range(len(output)):
                if (output[i].isdigit() and i == digitIndex) or (output[i].isalpha() and i == letterIndex):
                    continue
                outputIteration += output[i]
            output = outputIteration
        return output

    def hasDigit(self, s: str) -> bool:
        for char in s:
            if char.isdigit():
                return True
        return False


def test() -> None:
    solution = Solution()
    print(f'"{solution.clearDigits("cb34")}"')  # ""
    print(f'"{solution.clearDigits("abc3")}"')  # "ab"
    print(f'"{solution.clearDigits("abc")}"')  # "abc"


if __name__ == "__main__":
    test()
