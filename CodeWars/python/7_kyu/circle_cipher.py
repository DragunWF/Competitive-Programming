# https://www.codewars.com/kata/634d0723075de3f97a9eb604/train/python


def encode(s: str) -> str:
    encrypted_chars = []
    start_pointer = 0
    end_pointer = len(s) - 1
    while start_pointer <= end_pointer:
        encrypted_chars.append(s[start_pointer])
        if start_pointer == end_pointer:
            break
        encrypted_chars.append(s[end_pointer])
        start_pointer += 1
        end_pointer -= 1
    return "".join(encrypted_chars)


def decode(s: str) -> str:
    decrypted_chars_start = []
    decrypted_chars_end = []
    for i, char in enumerate(s):
        nth = i + 1
        if nth % 2 == 0:
            decrypted_chars_end.append(char)
        else:
            decrypted_chars_start.append(char)
    decrypted_chars_end.reverse()
    return "".join([*decrypted_chars_start, *decrypted_chars_end])


def test() -> None:
    TESTS = [
        ("codewars", "csordaew"),
        ("white", "wehti"),
        ("Assert", "Atsrse"),
        ("Hello world!", "H!edlllroo w"),
        ("You have chosen to translate this kata.", "Y.oaut ahka vsei hcth oesteanl stnoa rt"),
    ]
    correct_results = 0
    for i, item in enumerate(TESTS):
        initial_input = item[0]
        expected_plaintext = item[1]
        ciphertext = encode(initial_input)
        plaintext = decode(expected_plaintext)
        is_correct = plaintext == initial_input and ciphertext == expected_plaintext
        if is_correct:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {initial_input}, {expected_plaintext}")
        print(f"Encode Result: {ciphertext}")
        print(f"Decode Result: {plaintext}\n")
    print(f"Test Cases Passed: {correct_results}/{len(TESTS)}")


if __name__ == "__main__":
    print()
    test()
    print()
