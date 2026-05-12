# https://www.codewars.com/kata/589573e3f0902e8919000109/train/python

def shuffled_array(s: list[int]) -> list[int]:
    output = s.copy()
    output.sort()
    target = sum(s) // 2
    output.remove(target)
    return output


class TestCase:
    def __init__(self, s: list[int], expected: list[int]):
        self.s = s
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase([1, 12, 3, 6, 2], [1, 2, 3, 6]),
        TestCase([1, -3, -5, 7, 2], [-5, -3, 2, 7]),
        TestCase([2, -1, 2, 2, -1], [-1, -1, 2, 2]),
        TestCase([-3, -3], [-3])
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = shuffled_array(item.s)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.s}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
