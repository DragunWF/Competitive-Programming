# https://www.codewars.com/kata/56bf3287b5106eb10f000899/train/python

def move_vowels(input: str) -> str:
    VOWELS = "aeiou"
    vowels = []
    consonants = []
    for char in input:
        if char.lower() in VOWELS:
            vowels.append(char)
        else:
            consonants.append(char)
    return "".join(consonants) + "".join(vowels)


class TestCase:
    def __init__(self, text: str, expected: str):
        self.text = text
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("day", "dya"),
        TestCase("apple", "pplae"),
        TestCase('programming', 'prgrmmngoai')
    ]
    correct_results = 0
    for i, test_case in enumerate(test_cases):
        result = move_vowels(test_case.text)
        is_correct = test_case.expected == result
        if is_correct:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {test_case.text}")
        print(f"Result: {result}")
        print(f"Expected: {test_case.expected}")
        print()
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
