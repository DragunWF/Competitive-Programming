# https://www.codewars.com/kata/590938089ff3d186cb00004c/train/python

def suffix_sums(arr: list[int]) -> list[int]:
    total = sum(arr)
    sums = [total]
    for i in range(len(arr) - 1):
        total -= arr[i]
        sums.append(total)
    return sums


class TestCase:
    def __init__(self, arr: list[int], expected: list[int]):
        self.arr = arr
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase([1, 2, 3], [6, 5, 3]),
        TestCase([1, 2, 3, -6], [0, -1, -3, -6]),
        TestCase([0, 0, 0], [0, 0, 0]),
        TestCase([1, 123, 23], [147, 146, 23])
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = suffix_sums(item.arr)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.arr}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
