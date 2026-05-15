# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python

import math


def sum_for_list(nums: list[int]) -> list[list[int]]:
    prime_sums = {}
    for num in nums:
        factors = get_unique_prime_factors(num)
        for prime_num in factors:
            if not prime_num in prime_sums:
                prime_sums[prime_num] = 0
            prime_sums[prime_num] += num
    result = [[key, prime_sums[key]] for key in prime_sums]
    result.sort(key=lambda pair: pair[0])
    return result


def get_unique_prime_factors(n: int) -> int:
    n = abs(n)
    factors = set()

    if n % 2 == 0:
        factors.add(2)
        while n % 2 == 0:
            n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
    if n > 2:
        factors.add(n)
    return factors


class TestCase:
    def __init__(self, nums: list[int], expected: list[list[int]]):
        self.nums = nums
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase(
            [12, 15],
            [[2, 12], [3, 27], [5, 15]]
        ),
        TestCase(
            [15, 21, 24, 30, 45],
            [[2, 54], [3, 135], [5, 90], [7, 21]]
        ),
        TestCase(
            [15, 21, 24, 30, -45],
            [[2, 54], [3, 45], [5, 0], [7, 21]]
        ),
        TestCase(
            [107, 158, 204, 100, 118, 123, 126, 110, 116, 100],
            [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204],
                [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]
        ),
        TestCase(
            [-29804, -4209, -28265, -72769, -31744],
            [[2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744],
                [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804]]
        )
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = sum_for_list(item.nums)
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
