# https://www.codewars.com/kata/590c4c342ad5cd6a8700005c

def prefix_sums_to_suffix_sums(prefix_sums: list[int]) -> int:
    initial_arr = [prefix_sums[0]]
    for i in range(1, len(prefix_sums)):
        initial_arr.append(prefix_sums[i] - prefix_sums[i - 1])

    total = sum(initial_arr)
    suffix_sums = [total]
    for i in range(len(initial_arr) - 1):
        total -= initial_arr[i]
        suffix_sums.append(total)
    return suffix_sums


class TestCase:
    def __init__(self, prefix_sums: list[int], expected: list[int]):
        self.prefix_sums = prefix_sums
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase([1, 3, 6, 10, 15], [15, 14, 12, 9, 5]),
        TestCase([0], [0]),
        TestCase([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
        TestCase([1, -4, 2, 90, 100, -1], [-1, -2, 3, -3, -91, -101]),
        TestCase([1, 0, 1, 0, 1, 0, 1, 0], [0, -1, 0, -1, 0, -1, 0, -1]),
        TestCase([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        TestCase([0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = prefix_sums_to_suffix_sums(item.prefix_sums)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.prefix_sums}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
