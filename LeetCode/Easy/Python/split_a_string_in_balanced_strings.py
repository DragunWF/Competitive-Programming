# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_count = 0
        r_count = 0
        for char in s:
            if char == "R":
                r_count += 1
            else:
                r_count -= 1
            if r_count == 0:
                balanced_count += 1
        return balanced_count


class TestCase:
    def __init__(self, s: str, expected: int):
        self.s = s
        self.expected = expected


def test() -> None:
    test_cases: list[TestCase] = [
        TestCase("RLRRLLRLRL", 4),
        TestCase("RLRRRLLRLL", 2),
        TestCase("LLLLRRRR", 1)
    ]
    correct_count = 0
    solution = Solution()
    for i, item in enumerate(test_cases):
        result = solution.balancedStringSplit(item.s)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.s}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
