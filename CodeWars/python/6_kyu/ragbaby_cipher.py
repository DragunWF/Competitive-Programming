# https://www.codewars.com/kata/5a2166f355519e161a000019

from string import ascii_uppercase, ascii_lowercase


def encode(text: str, key: str) -> str:
    return operate_cipher(text, key, True)


def decode(text: str, key: str) -> str:
    return operate_cipher(text, key, False)


def operate_cipher(text: str, key: str, is_encryption: bool) -> str:
    cipher_map = generate_cipher_map(key)
    shifted_chars = []
    char_pos = 0
    for char in text:
        if not char.isalpha():
            char_pos = 0
            shifted_chars.append(char)
            continue

        indices = cipher_map["upper_indices" if char.isupper() else "lower_indices"]
        current_map = cipher_map["upper" if char.isupper() else "lower"]

        shifted_index = None
        if is_encryption:
            shifted_index = (indices[char] + char_pos + 1) % len(indices)
        else:
            shifted_index = (indices[char] - (char_pos + 1)) % len(indices)

        shifted_chars.append(current_map[shifted_index])
        char_pos += 1
    return "".join(shifted_chars)


def generate_cipher_map(key: str) -> dict:
    unique_in_order = []
    for char in key:
        if not char in unique_in_order:
            unique_in_order.append(char)
    key = "".join(unique_in_order)

    uppercase = key.upper() + "".join(char for char in ascii_uppercase if not char in key.upper())
    lowercase = key + "".join(char for char in ascii_lowercase if not char in key)
    return {"upper_indices": map_indices(uppercase),
            "upper": uppercase,
            "lower_indices": map_indices(lowercase),
            "lower": lowercase}


def map_indices(pool: str) -> dict:
    mapped_indicies = {}
    for i, char in enumerate(pool):
        mapped_indicies[char] = i
    return mapped_indicies


class TestCase:
    def __init__(self, text: str, key: str, expected: str):
        self.text = text
        self.key = key
        self.expected = expected


def test() -> None:
    encryption_test_cases = [
        TestCase("cipher", "cipher", "ihrbfj"),
        TestCase("cipher", "cccciiiiippphheeeeerrrrr", "ihrbfj"),
        TestCase("This is an example.", "cipher", "Urew pu bq rzfsbtj."),
        TestCase("This.tHis.thIs.thiS...", "cipher", "Urew.uRew.urEw.ureW...")
    ]
    print("+ ================ Encryption Test Cases ================ +\n")
    test_func(encryption_test_cases, encode)
    decryption_test_cases = []
    for test_case in encryption_test_cases:
        decryption_test_cases.append(
            TestCase(test_case.expected, test_case.key, test_case.text)
        )
    print("\n+ ================ Decryption Test Cases ================ +\n")
    test_func(decryption_test_cases, decode)


def test_func(test_cases: list[TestCase], func) -> None:
    correct_results = 0
    for i, test_case in enumerate(test_cases):
        result = func(test_case.text, test_case.key)
        is_correct = result == test_case.expected
        if is_correct:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {test_case.text}, {test_case.key}")
        print(f"Result: {result}")
        print(f"Expected: {test_case.expected}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
