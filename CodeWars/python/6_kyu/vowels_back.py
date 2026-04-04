# https://www.codewars.com/kata/57cfd92c05c1864df2001563/python

from string import ascii_lowercase


def vowel_back(s: str) -> str:
    VOWELS = "aiu"
    EXCEPTIONS = "code"

    output = []
    for char in s:
        ascii_pos = ord(char) - 97
        if char in VOWELS:
            ascii_pos -= 5
        elif char == "c" or char == "o":
            ascii_pos -= 1
        elif char == "d":
            ascii_pos -= 3
        elif char == "e":
            ascii_pos -= 4
        else:
            ascii_pos += 9

        ascii_pos %= len(ascii_lowercase)
        new_char = ascii_lowercase[ascii_pos]
        output.append(char if new_char in EXCEPTIONS else ascii_lowercase[ascii_pos])

    return "".join(output)


class TestCase:
    def __init__(self, text: str, expected: str):
        self.text = text
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("testcase", "tabtbvba"),
        TestCase("codewars", "bnaafvab"),
        TestCase("exampletesthere", "agvvyuatabtqaaa")
    ]
    correct_results = 0
    for i, item in enumerate(test_cases):
        result = vowel_back(item.text)
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
