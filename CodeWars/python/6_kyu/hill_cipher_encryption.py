# https://www.codewars.com/kata/5e958a9bbb01ec000f3c75d8/train/python

from string import ascii_uppercase


def encrypt(text: str, key: str) -> str:
    if not text:
        return ""

    text = [char for char in text.upper() if char.isalpha()]
    pairs = []
    current_pair = []
    for char in text:
        current_pair.append(ord(char) - 65)
        if len(current_pair) == 2:
            pairs.append(current_pair.copy())
            current_pair.clear()
    if len(current_pair) == 1:
        pairs.append([current_pair[0], 25])

    matrix_key = to_matrix_key(key)
    encrypted_chars = []
    for pair in pairs:
        first_result = (pair[0] * matrix_key[0][0] + pair[1] * matrix_key[0][1]) % 26
        second_result = (pair[0] * matrix_key[1][0] + pair[1] * matrix_key[1][1]) % 26
        encrypted_chars.append(ascii_uppercase[first_result])
        encrypted_chars.append(ascii_uppercase[second_result])
    return "".join(encrypted_chars)


def to_matrix_key(key: str) -> list[list[int]]:
    key = key.upper()
    matrix_key = [[], []]
    for i, char in enumerate(key):
        letter_index = ord(char) - 65
        matrix_key[int(i > 1)].append(letter_index)
    return matrix_key


def test() -> None:
    test_cases = [
        {"text": "", "key": "ayzb", "expected": ""},
        {"text": "Hi", "key": "cats", "expected": "OR"},
        {"text": "This is a good day", "key": "bbaa", "expected": 'AAAAAAGACAGAYA'}
    ]
    correct_results = 0
    for i, test_case in enumerate(test_cases):
        result = encrypt(test_case["text"], test_case["key"])
        is_passed = result == test_case["expected"]
        if is_passed:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_passed else 'Failed'}")
        print(f"Input: {test_case["text"]} (text) | {test_case["key"]} (key)")
        print(f"Result: {result}")
        print(f"Expected: {test_case['expected']}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    test()
