# https://www.codewars.com/kata/55ee3ebff71e82a30000006a/train/python

from string import ascii_uppercase


def title_to_number(title: str) -> int:
    alphabet_map = create_alphabet_map()
    letters = [*title]
    letters.reverse()
    column_num = 0
    for i, letter in enumerate(letters):
        if i == 0:
            column_num += alphabet_map[letter]
        else:
            column_num += alphabet_map[letter] * 26 ** i
    return column_num


def create_alphabet_map() -> dict:
    output = {}
    for i, char in enumerate(ascii_uppercase):
        output[char] = i + 1
    return output


class TestCase:
    def __init__(self, title: str, expected: int):
        self.title = title
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("A", 1),
        TestCase("Z", 26),
        TestCase("BA", 53),
        TestCase("CODEWARS", 28779382963),
        TestCase('OYAJI', 7294985)
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = title_to_number(item.title)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.title}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
