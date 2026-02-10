# https://www.codewars.com/kata/5508249a98b3234f420000fb/train/python

import math
from string import ascii_lowercase, ascii_uppercase


def moving_shift(s: str, shift: int) -> list[str]:
    CHUNK_COUNT = 5

    encrypted_chars = []
    for char in s:
        if not is_plaintext_char(char):
            encrypted_chars.append(char)
        else:
            normalized_index = ord(char.upper()) - 65
            shifted_index = (normalized_index + shift) % 26
            if char.isupper():
                encrypted_chars.append(ascii_uppercase[shifted_index])
            else:
                encrypted_chars.append(ascii_lowercase[shifted_index])
        shift += 1

    encrypted_chunks = []
    chunk_length = math.ceil(len(s) / CHUNK_COUNT)
    current_index = 0
    for i in range(5):
        if current_index >= len(s):
            encrypted_chunks.append("")
            continue
        chunk = "".join(encrypted_chars[current_index:current_index + chunk_length])
        encrypted_chunks.append(chunk)
        current_index = current_index + chunk_length

    return encrypted_chunks


def demoving_shift(s: list[str], shift: int) -> str:
    decrypted_chars = []
    for part in s:
        for char in part:
            if not is_plaintext_char(char):
                decrypted_chars.append(char)
            else:
                normalized_index = ord(char.upper()) - 65
                shifted_index = (normalized_index - shift) % 26
                if char.isupper():
                    decrypted_chars.append(ascii_uppercase[shifted_index])
                else:
                    decrypted_chars.append(ascii_lowercase[shifted_index])
            shift += 1
    return "".join(decrypted_chars)


def is_plaintext_char(char: str) -> bool:
    return char in ascii_lowercase or char in ascii_uppercase


def test() -> None:
    wall = "-" * 100
    encryption_test_cases = [
        {"s": "I should have known that you would have a perfect answer for me!!!",
         "shift": 1,
         "expected": ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]},
        {"s": "How can we become the kind of people that face our fear and do it anyway?",
         "shift": 1,
         "expected": ["Iqz hgu fo nrqd", "cv mbz hgmd qi ", "ukvxuo fuoi wsv", "y krp ffcu ftk ", "my ug pdpots?"]},
        {"s": " uoxIirmoveNreefckgieaoiEcooqo",
         "shift": 2,
         "expected": [' xscOp', 'zvygqA', 'ftuwud', 'adaxmh', 'Edqrut']}
    ]

    print("+ ========== Encryption Tests ========== +")
    encryption_test_cases_passes = 0
    for i, test_case in enumerate(encryption_test_cases):
        result = moving_shift(test_case["s"], test_case["shift"])
        is_passed = result == test_case["expected"]
        if is_passed:
            encryption_test_cases_passes += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_passed else 'Failed'}")
        print(f"Input: {test_case["s"]}")
        print(f"Result: {result}")
        print(f"Expected: {test_case["expected"]}\n{wall}")
    print(f"Test cases passed (Encryption): {encryption_test_cases_passes}/{len(encryption_test_cases)}")

    decryption_test_cases = [
        {"s": encryption_test_cases[0]["expected"],
         "shift": encryption_test_cases[0]["shift"],
         "expected": encryption_test_cases[0]["s"]},
        {"s": encryption_test_cases[1]["expected"],
         "shift": encryption_test_cases[1]["shift"],
         "expected": encryption_test_cases[1]["s"]},
        {"s": encryption_test_cases[2]["expected"],
         "shift": encryption_test_cases[2]["shift"],
         "expected": encryption_test_cases[2]["s"]},
    ]

    print("\n+ ========== Decryption Tests ========== +")
    decryption_test_cases_passes = 0
    for i, test_case in enumerate(decryption_test_cases):
        result = demoving_shift(test_case["s"], test_case["shift"])
        is_passed = result == test_case["expected"]
        if is_passed:
            decryption_test_cases_passes += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_passed else 'Failed'}")
        print(f"Input: {test_case["s"]}")
        print(f"Result: {result}")
        print(f"Expected: {test_case['expected']}\n{wall}")
    print(f"Test cases passed (Decryption): {decryption_test_cases_passes}/{len(decryption_test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
