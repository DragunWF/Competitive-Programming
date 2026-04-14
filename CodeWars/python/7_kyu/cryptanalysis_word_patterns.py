# https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e/train/javascript

def word_pattern(word: str) -> str:
    word = word.lower()
    appearance = {}
    for i, char in enumerate(word):
        if not char in appearance:
            appearance[char] = str(len(appearance.keys()))
    return ".".join([appearance[char] for char in word])


class TestCase:
    def __init__(self, word: str, expected: str):
        self.word = word
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("hello", "0.1.2.2.3"),
        TestCase("heLlo", "0.1.2.2.3"),
        TestCase("helLo", "0.1.2.2.3"),
        TestCase("Hippopotomonstrosesquippedaliophobia",
                 "0.1.2.2.3.2.3.4.3.5.3.6.7.4.8.3.7.9.7.10.11.1.2.2.9.12.13.14.1.3.2.0.3.15.1.13")
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = word_pattern(item.word)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.word}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
