# https://www.codewars.com/kata/55e29a6b4d99b59e98000089

from math import sqrt


def ascii_cipher(message: str, key: int) -> str:
    ciphertext = []
    largest_prime_factor = get_largest_prime_factor(abs(key))
    if key < 0:
        largest_prime_factor = -largest_prime_factor
    for char in message:
        ciphertext.append(chr((ord(char) + largest_prime_factor) % 128))
    return "".join(ciphertext)


def get_largest_prime_factor(num: int) -> int:
    max_prime = -1
    while num % 2 == 0:
        max_prime = 2
        num //= 2
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            max_prime = i
            num //= i
    if num > 2:
        max_prime = num
    return max_prime


class TestCase:
    def __init__(self, message: str, key: int, expected: str):
        self.message = message
        self.key = key
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("Hello, world", 18, "Khoor/#zruog"),
        TestCase("Encryption rules!", 326, "hCD"),
        TestCase("Imitation Game, up in here!", -7, "BfbmZmbhg@Zf^%nibga^k^")
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        ciphertext = ascii_cipher(item.message, item.key)
        is_correct = ciphertext == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.message}, {item.key}")
        print(f"Result: {ciphertext}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
