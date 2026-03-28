# https://www.codewars.com/kata/585db3e8eec141ce9a00008f/train/python

def reverse_vowels(s: str) -> str:
    vowels = []
    positions = []
    for i, char in enumerate(s):
        if char.lower() in "aeiou":
            vowels.append(char)
            positions.append(i)
    return reverse_vowels_in_sentence(s, vowels, positions)


def reverse_vowels_in_sentence(sentence: str, vowels: list[str], positions: list[int]) -> str:
    vowels.reverse()
    reversed = []
    current_vowel_index = 0
    for i, char in enumerate(sentence):
        if i in positions:
            reversed.append(vowels[current_vowel_index])
            current_vowel_index += 1
            continue
        reversed.append(char)
    return "".join(reversed)


class TestCase:
    def __init__(self, text: str, expected: str):
        self.text = text
        self.expected = expected


def test() -> None:
    test_cases: list[TestCase] = [
        TestCase("Hello!", "Holle!"),
        TestCase("Tomatoes", "Temotaos"),
        TestCase("Reverse Vowels In A String", "RivArsI Vewols en e Streng")
    ]
    correct_results = 0
    for i, item in enumerate(test_cases):
        result = reverse_vowels(item.text)
        is_correct = result == item.expected
        if is_correct:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.text}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}")
        print()
    print(f"\nTest Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
