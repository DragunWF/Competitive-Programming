# https://www.codewars.com/kata/59eb28fb0a2bffafbb0000d6/train/python

def sort_by_binary_ones(num_list: list[int]) -> list[int]:
    num_list.sort(reverse=True, key=lambda num: bin(num).count("1"))
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - 1):
            current_bin = bin(num_list[j])
            next_bin = bin(num_list[j + 1])
            current = current_bin.count("1")
            next = next_bin.count("1")
            if current == next:
                if (len(current_bin) > len(next_bin) or (len(current_bin) == len(next_bin) and num_list[j] > num_list[j + 1])):
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
            elif current < next:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


class TestCase:
    def __init__(self, num_list: list[int], expected: list[int]):
        self.num_list = num_list
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase([1, 15, 5, 7, 3], [15, 7, 3, 5, 1]),
        TestCase([1, 3], [3, 1]),
        TestCase([1, 2, 3, 4], [3, 1, 2, 4]),
        TestCase([1, 2, 3, 4], [3, 1, 2, 4]),
        TestCase([1, 3], [3, 1]),
        TestCase([1, 15, 7, 3, 5], [15, 7, 3, 5, 1]),
        TestCase([80, 21], [21, 80]),
        TestCase([0, 1024, 33], [33, 1024, 0]),
        TestCase([2, 2048, 3], [3, 2, 2048]),
        TestCase([5, 2049, 3], [3, 5, 2049]),
        TestCase([1, 5, 21, 7, 44, 99, 50, 51, 49, 80, 33, 25], [51, 99, 7, 21, 25, 44, 49, 50, 5, 33, 80, 1])
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = sort_by_binary_ones(item.num_list.copy())
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.num_list}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
