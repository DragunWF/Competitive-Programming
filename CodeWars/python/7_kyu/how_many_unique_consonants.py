# https://www.codewars.com/kata/5a19226646d843de9000007d

def count_consonants(text: str) -> int:
    unique_consonants = set()
    for char in text.lower():
        if not char in "aeiou" and char.isalpha():
            unique_consonants.add(char)
    return len(unique_consonants)


class TestCase:
    def __init__(self, text: str, expected: int):
        self.text = text
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("add", 1),
        TestCase("Dad", 1),
        TestCase("aeiou", 0),
        TestCase("sillystring", 7),
        TestCase("abcdefghijklmnopqrstuvwxyz", 21),
        TestCase("Count my unique consonants!!", 7)
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = count_consonants(item.text)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.text}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
