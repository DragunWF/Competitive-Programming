# https://leetcode.com/problems/count-elements-with-maximum-frequency

from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = self.createCounter(nums)
        max_frequency = max(frequencies[frequency] for frequency in frequencies)
        count = 0
        for value in frequencies.values():
            if value == max_frequency:
                count += max_frequency
        return count

    def createCounter(self, nums: List[int]) -> dict[int, int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        return counter


class TestCase:
    def __init__(self, nums: List[int], expected: int):
        self.nums = nums
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase([1, 2, 2, 3, 1, 4], 4),
        TestCase([1, 2, 3, 4, 5], 5)
    ]
    correct_count = 0
    solution = Solution()
    for i, item in enumerate(test_cases):
        result = solution.maxFrequencyElements(item.nums)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.nums}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
