# https://www.codewars.com/kata/542a823c909c97da4500055e

def polybius(text: str) -> str:
    alphabet_key = {
        "A": "11", "B": "12", "C": "13", "D": "14", "E": "15",
        "F": "21", "G": "22", "H": "23", "I": "24", "J": "24", "K": "25",
        "L": "31", "M": "32", "N": "33", "O": "34", "P": "35",
        "Q": "41", "R": "42", "S": "43", "T": "44", "U": "45",
        "V": "51", "W": "52", "X": "53", "Y": "54", "Z": "55"
    }
    encrypted_chars = []
    for char in text:
        if not char in alphabet_key:
            encrypted_chars.append(char)
            continue
        encrypted_chars.append(alphabet_key[char])
    return "".join(encrypted_chars)


class TestCase:
    def __init__(self, text: str, expected: str):
        self.text = text
        self.expected = expected


def test() -> None:
    test_cases: list[TestCase] = [
        TestCase("A", "11"),
        TestCase("IJ", "2424"),
        TestCase("CODEWARS", "1334141552114243"),
        TestCase("POLYBIUS SQUARE CIPHER", "3534315412244543 434145114215 132435231542")
    ]
    correct_results = 0
    for i, test_case in enumerate(test_cases):
        result = polybius(test_case.text)
        is_passed = result == test_case.expected
        if is_passed:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_passed else 'Failed'}")
        print(f"Input: {test_case.text}")
        print(f"Result: {result}")
        print(f"Expected: {test_case.expected}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    test()
