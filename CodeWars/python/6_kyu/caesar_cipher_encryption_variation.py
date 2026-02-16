# https://www.codewars.com/kata/55ec55323c89fc5fbd000019

from string import ascii_lowercase


def caesar_encode(phrase: str, shift: int) -> str:
    alphabet_map = create_alphabet_map()
    encrypted_words = []
    words = phrase.split(" ")
    for i, word in enumerate(words):
        encrypted_chars = []
        for char in word:
            shifted_index = (alphabet_map[char] + shift + i) % 26
            encrypted_chars.append(ascii_lowercase[shifted_index])
        encrypted_words.append("".join(encrypted_chars))
    return " ".join(encrypted_words)


def create_alphabet_map() -> dict:
    alphabet_map = {}
    for i, char in enumerate(ascii_lowercase):
        alphabet_map[char] = i
    return alphabet_map


class TestCase:
    def __init__(self, phrase: str, shift: int, expected: str):
        self.phrase = phrase
        self.shift = shift
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase("alea iacta est", 3, "dohd megxe jxy"),
        TestCase("conquer et impera", 13, "pbadhre sh xbetgp"),
        TestCase("fere libenter homines id quod volunt credunt", 7, "mlyl tqjmvbmz qxvrwnb sn bfzo haxgzf perqhag"),
        TestCase("horum omnium fortissimi sunt belgae", 0, "horum pnojvn hqtvkuukok vxqw fipkei")
    ]
    correct_results = 0
    for i, test_case in enumerate(test_cases):
        result = caesar_encode(test_case.phrase, test_case.shift)
        is_correct = result == test_case.expected
        if is_correct:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {test_case.phrase}, {test_case.shift}")
        print(f"Result: {result}")
        print(f"Expected: {test_case.expected}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
