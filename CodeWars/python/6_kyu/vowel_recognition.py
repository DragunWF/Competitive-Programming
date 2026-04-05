# https://www.codewars.com/kata/5bed96b9a68c19d394000b1d/train/python

def vowel_recognition(s: str) -> int:
    VOWELS = "aeiou"
    total = 0
    for i, char in enumerate(s.lower()):
        if char in VOWELS:
            total += (i + 1) * (len(s) - i)
    return total


class TestCase:
    def __init__(self, text: str, expected: int):
        self.text = text
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("bbbb", 0),
        TestCase("baceb", 16),
        TestCase("aeiou", 35),
        TestCase("aeiouAEIOU", 220)
    ]
    correct_results = 0
    for i, item in enumerate(test_cases):
        result = vowel_recognition(item.text)
        is_correct = result == item.expected
        if is_correct:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.text}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
