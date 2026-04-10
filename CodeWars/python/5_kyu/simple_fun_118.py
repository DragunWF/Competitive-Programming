# https://www.codewars.com/kata/589d581680458f695200008e/train/python

def sum_or_product(arr: list[int]) -> int:
    if len(arr) == 1:
        return arr[0]

    ones_count = arr.count(1)
    others = [x for x in arr if x > 1]

    for i in range(len(others)):
        if others[i] == 2 and ones_count > 0:
            others[i] = 3
            ones_count -= 1

    while ones_count >= 3:
        others.append(3)
        ones_count -= 3

    if ones_count == 2:
        others.append(2)
    elif ones_count == 1:
        if not others:
            return 1
        min_index = others.index(min(others))
        others[min_index] += 1

    product = 1
    for num in others:
        product *= num

    return product


def sum_or_product_old(arr: list):
    if len(arr) == 1:
        return arr[0]

    nums = arr.copy()
    while 1 in nums:
        index_of_one = nums.index(1)
        min_num_index = get_min_num_index(nums, index_of_one)
        nums[min_num_index] += 1
        nums.pop(index_of_one)

    product = nums[0]
    for i, num in enumerate(nums):
        if i == 0:
            continue
        product *= num
    return product


def get_min_num_index(arr: list[int], avoid_index: int) -> tuple[int, int]:
    min_num = None
    min_index = None
    for i, num in enumerate(arr):
        if i == avoid_index:
            continue
        if min_num is None or num < min_num:
            min_num = num
            min_index = i
    return min_index


class TestCase:
    def __init__(self, arr: list[int], expected: int):
        self.arr = arr
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase([1, 2, 3], 9),
        TestCase([1, 1, 2], 4),
        TestCase([1, 1, 1], 3),
        TestCase([1], 1),
        TestCase([9], 9),
        TestCase([1, 1], 2),
        TestCase([1, 5], 6),
        TestCase([1, 5, 7], 42),
        TestCase([1, 5, 6], 36),
        TestCase([1, 1, 5, 7], 70),
        TestCase([1, 1, 1, 1], 4),
        TestCase([1, 1, 1, 1, 1], 6),
        TestCase([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1458),
        TestCase([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 972),
        TestCase([1, 1, 2, 4, 5], 80),
        TestCase([10, 20, 30], 6000)
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = sum_or_product(item.arr)
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
