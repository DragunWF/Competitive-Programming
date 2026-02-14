# https://www.codewars.com/kata/671bd5419ea261fbb8d0a0ca

import math
from string import ascii_lowercase


def decipher(code: list[str]) -> str:
    if len(code) == 1:
        return code[0]
    output = []
    for i in range(len(code[0])):
        total = 0
        for item in code:
            if item[i] == " ":
                continue
            total += ord(item[i].upper()) - 64
        average = math.floor(total / len(code))
        output.append(" " if not average else ascii_lowercase[average - 1])
    return "".join(output)


def test() -> None:
    # Test-Driven Development (TDD)???? waw
    test_cases = [
        {"code": ["u lk zxuq hfk as fouh", "y l  zpuv  xe at sicd", "welvayfuqbfpeaauaqcrc"],
         "expected": "walk your dog at nine"},
        {"code": ["foreman pig", "foreman pig"],
         "expected": "foreman pig"},
        {"code": ["hello world"],
         "expected": "hello world"}
    ]
    correct_results = 0
    for i, test_case in enumerate(test_cases):
        result = decipher(test_case['code'])
        is_passed = result == test_case['expected']
        if is_passed:
            correct_results += 1
        print(f"Test Case #{i + 1}:")
        print(f"Input: {test_case['code']}")
        print(f"Result: {result}")
        print(f"Expected: {test_case['expected']}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
