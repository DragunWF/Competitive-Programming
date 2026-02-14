# https://www.codewars.com/kata/5558cc216a7a231ac9000022/train/python

def duplicates(arr: list) -> list:
    counter = {}
    duplicate_items = []
    for char in arr:
        if not char in counter:
            counter[char] = 1
        else:
            counter[char] += 1
            if counter[char] >= 2 and not char in duplicate_items:
                duplicate_items.append(char)
    return duplicate_items


def test() -> None:
    test_cases = [
        {"arr": [1, 2, 4, 4, 3, 3, 1, 5, 3, "5"], "expected": [4, 3, 1]},
        {"arr": [0, 1, 2, 3, 4, 5], "expected": []}
    ]
    correct_results = 0
    for i, test_case in enumerate(test_cases):
        result = duplicates(test_case["arr"])
        is_passed = result == test_case["expected"]
        if is_passed:
            correct_results += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_passed else 'Failed'}")
        print(f"Input: {test_case['arr']}")
        print(f"Result: {result}")
        print(f"Expected: {test_case['expected']}\n")
    print(f"Test Cases Passed: {correct_results}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
