# https://www.codewars.com/kata/5a71939d373c2e634200008e/train/java

def solve(s: str) -> str:
    reversed_letters = []
    for char in s:
        if char.isalpha():
            reversed_letters.append(char)
    reversed_letters.reverse()

    output = []
    current_letter_index = 0
    for char in s:
        if char.isalpha():
            output.append(reversed_letters[current_letter_index])
            current_letter_index += 1
        else:
            output.append(char)
    return "".join(output)


def test() -> None:
    test_cases = [
        {"s": "our code", "expected": "edo cruo"},
        {"s": "your code rocks", "expected": "skco redo cruoy"},
        {"s": "codewars", "expected": "srawedoc"}
    ]
    correct_results_count = 0
    for i, test_case in enumerate(test_cases):
        result = solve(test_case["s"])
        is_passed = result == test_case["expected"]
        if is_passed:
            correct_results_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_passed else 'Failed'}")
        print(f"Input: {test_case['s']}")
        print(f"Result: {result}")
        print(f"Expected: {test_case['expected']}\n")
    print(f"Test Cases Passed: {correct_results_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
