# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

def sum_pairs(nums: list, target: int) -> list[int, int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [complement, num]
        if not num in seen:
            seen[num] = i


def sum_pairs_brute_force(nums: list, target: int) -> list[int, int]:
    # Alternative solution that will definitely time out
    N = len(nums)
    dp = {}
    candidates = []

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            # Check pair (permutation considered) in calculated values
            if (i, j) in dp or (j, i) in dp:
                continue

            result = nums[i] + nums[j]
            if result == target:
                candidates.append(
                    {"pair": [nums[i], nums[j]],
                     "second_index": j}
                )
            dp[(i, j)] = result
            dp[(j, i)] = result

    if candidates:
        return get_min_pair(candidates)

    return None


def get_min_pair(candidates: list[dict]) -> list:
    min_pair = None
    min_index = None
    for candidate in candidates:
        if min_index is None or candidate["second_index"] < min_index:
            min_pair = candidate["pair"]
            min_index = candidate["second_index"]
    return min_pair


class TestCase:
    def __init__(self, nums: list[int], target: int, expected: list[int]):
        self.nums = nums
        self.target = target
        self.expected = expected

    def __str__(self) -> str:
        return f"nums: {self.nums}\ntarget: {self.target}"


def test() -> None:
    test_cases = [
        TestCase([11, 3, 7, 5], 10, [3, 7]),
        TestCase([4, 3, 2, 3, 4], 6, [4, 2]),
        TestCase([0, 0, -2, 3], 2, None),
        TestCase([10, 5, 2, 3, 7, 5], 10, [3, 7])
    ]
    print("Test Cases:\n------------------------------")
    for item in test_cases:
        result = sum_pairs(item.nums, item.target)
        print(f"Test Case:\n{item}")
        print(f"Result: {result} | Pass: {result == item.expected}\n")
    print("-----------------------------")


if __name__ == "__main__":
    test()
