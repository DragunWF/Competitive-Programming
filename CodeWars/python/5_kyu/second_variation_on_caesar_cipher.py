# https://www.codewars.com/kata/55084d3898b323f0aa000546/train/python

import math
from string import ascii_uppercase, ascii_lowercase


def encode_str(s: str, shift: int) -> str:
    CHUNK_COUNT = 5

    encrypted_chars = []
    for i, char in enumerate(s):
        if not is_plaintext_char(char):
            encrypted_chars.append(char)
            continue

        current_index = ord(char.upper()) - 65
        shifted_index = (current_index + shift) % 26
        if i == 0:
            encrypted_chars.append(char.lower())
            encrypted_chars.append(ascii_lowercase[shifted_index])
        if char.isupper():
            encrypted_chars.append(ascii_uppercase[shifted_index])
        else:
            encrypted_chars.append(ascii_lowercase[shifted_index])

    encrypted_chunks = []
    chunk_length = math.ceil(len(encrypted_chars) / CHUNK_COUNT)
    current_index = 0
    for i in range(CHUNK_COUNT):
        if current_index >= len(encrypted_chars):
            break
        chunk = "".join(encrypted_chars[current_index:current_index + chunk_length])
        encrypted_chunks.append(chunk)
        current_index = current_index + chunk_length

    return encrypted_chunks


def decode(arr: list[str]) -> str:
    first_chunk = arr[0]
    shift = ord(first_chunk[1]) - ord(first_chunk[0])

    decrypted_chars = []
    for i, chunk in enumerate(arr):
        if i == 0:
            chunk = chunk[2:]
        for char in chunk:
            if not is_plaintext_char(char):
                decrypted_chars.append(char)
                continue
            current_index = ord(char.upper()) - 65
            shifted_index = (current_index - shift) % 26
            if char.isupper():
                decrypted_chars.append(ascii_uppercase[shifted_index])
            else:
                decrypted_chars.append(ascii_lowercase[shifted_index])
    return "".join(decrypted_chars)


def is_plaintext_char(char: str) -> bool:
    return char in ascii_lowercase or char in ascii_uppercase


def test() -> None:
    encryption_test_cases = [
        {
            "s": "I should have known that you would have a perfect answer for me!!!",
            "shift": 1,
            "expected": ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ", "b qfsgfdu botx", "fs gps nf!!!"]
        },
        {
            "s": "abcdefghjuty12",
            "shift": 1,
            "expected": ['abbc', 'defg', 'hikv', 'uz12']
        },
        {
            "s": "abcdefghjuty12",
            "shift": 30,
            "expected": ['aeef', 'ghij', 'klny', 'xc12']
        }
    ]
    print("+ ============ Encryption Test Cases ============ +")
    test_func(encryption_test_cases, encode_str, True)
    decryption_test_cases = []
    for test_case in encryption_test_cases:
        decryption_test_cases.append({
            "s": test_case["expected"],
            "expected": test_case["s"]
        })
    print("\n+ ============ Decryption Test Cases ============ +")
    test_func(decryption_test_cases, decode, False)


def test_func(test_cases: list[dict], func, is_two_parameters: bool) -> None:
    correct_results = 0
    for i, test_case in enumerate(test_cases):
        result = None
        if is_two_parameters:
            result = func(test_case["s"], test_case["shift"])
        else:
            result = func(test_case["s"])

        is_passed = result == test_case["expected"]
        if is_passed:
            correct_results += 1
        print(f"Test Case #{i + 1}: ")
        print(f"Input: {test_case['s']}")
        print(f"Result: {result}")
        print(f"Expected: {test_case['expected']}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    test()
