# https://www.codewars.com/kata/54d3bb4dfc75996c1c000c6d

def midpoint_sum(nums: list[int]):
    for i in range(1, len(nums) - 1):
        left_side_sum = sum(nums[:i])
        right_side_sum = sum(nums[i + 1:])
        if left_side_sum == right_side_sum:
            return i
    return -1


def test() -> None:
    # Expected: 3
    print(midpoint_sum([4, 1, 7, 9, 3, 9]))

    # Expected: None
    print(midpoint_sum([1, 0, -1]))


if __name__ == "__main__":
    test()
