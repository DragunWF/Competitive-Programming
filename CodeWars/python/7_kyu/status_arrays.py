# https://www.codewars.com/kata/601c18c1d92283000ec86f2b

def status(nums: list[int]) -> list[int]:
    output = []
    status_values = []
    for i, num in enumerate(nums):
        status_value = get_all_higher(nums, num, i) + i
        status_values.append((i, status_value))
    status_values.sort(key=lambda x: (x[1], x[0]))
    for value in status_values:
        output.append(nums[value[0]])
    return output


def get_all_higher(nums: list[int], current_num: int, pos: int) -> int:
    higher_elements_count = 0
    for i, num in enumerate(nums):
        if i == pos:
            continue
        if current_num > num:
            higher_elements_count += 1
    return higher_elements_count


class TestCase:
    def __init__(self, nums: list[int], expected: list[int]):
        self.nums = nums
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase([6, 9, 3, 8, 2, 3, 1], [6, 3, 2, 1, 9, 3, 8]),
        TestCase([5, 5, 5, 8, 7, -2, -2, -3, 1, 9, 8, 3, -3, 4, -4, 6],
                 [5, -2, -3, 5, -2, 5, 1, -3, -4, 8, 7, 3, 4, 8, 9, 6]),
        TestCase([14, -3, 4, 6, 9, 10, -2, 4, 0], [-3, 4, -2, 14, 6, 9, 4, 0, 10])
    ]
    correct_count = 0
    for i, test_case in enumerate(test_cases):
        result = status(test_case.nums)
        is_correct = result == test_case.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {test_case.nums}")
        print(f"Result: {result}")
        print(f"Expected: {test_case.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
