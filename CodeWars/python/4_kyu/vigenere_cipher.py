# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3

class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.key = key
        self.alphabet = alphabet
        self.alphabet_map = {}
        for i, char in enumerate(alphabet):
            self.alphabet_map[char] = i

    def encode(self, text: str) -> str:
        return self.__operate(text, True)

    def decode(self, text: str) -> str:
        return self.__operate(text, False)

    def __operate(self, text: str, is_encryption: bool) -> str:
        output = []
        for i, char in enumerate(text):
            if not char in self.alphabet:
                output.append(char)
                continue
            key_char = self.key[i % len(self.key)]
            new_char_index = None
            if is_encryption:
                new_char_index = (self.alphabet_map[char] + self.alphabet_map[key_char]) % len(self.alphabet)
            else:
                new_char_index = (self.alphabet_map[char] - self.alphabet_map[key_char]) % len(self.alphabet)
            output.append(self.alphabet[new_char_index])
        return "".join(output)


def test() -> None:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "password"

    test_cases = [
        {"plaintext": "codewars", "ciphertext": "rovwsoiv"},
        {"plaintext": "waffles", "ciphertext": "laxxhsj"},
        {"plaintext": "CODEWARS", "ciphertext": "CODEWARS"}
    ]
    correct_results = 0
    cipher = VigenereCipher(key, alphabet)
    print("+ ======== Vigenere Cipher ======== +")
    print(f"Input: {alphabet} (alphabet) | {key} (key)\n")
    for i, test_case in enumerate(test_cases):
        encoded_result = cipher.encode(test_case["plaintext"])
        decoded_result = cipher.decode(test_case["ciphertext"])
        is_encryption_correct = encoded_result == test_case["ciphertext"]
        is_decryption_correct = decoded_result == test_case["plaintext"]

        if is_encryption_correct and is_decryption_correct:
            correct_results += 1

        print(f"+ ======== Test Case {i + 1}: ======== +")
        print(f"Encoded Result: {encoded_result} | {test_case_status(is_encryption_correct)}")
        print(f"Decoded Result: {decoded_result} | {test_case_status(is_decryption_correct)}")
        print(f"Expected Plaintext: {test_case["plaintext"]}")
        print(f"Expected Ciphertext: {test_case["ciphertext"]}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


def test_case_status(status: bool) -> str:
    return "Passed" if status else "Failed"


if __name__ == "__main__":
    print()
    test()
    print()
