# https://www.codewars.com/kata/57f5e7bd60d0a0cfd900032d/train/python

def missing_no(nums: list[int]):
    nums.sort()
    if nums[0] != 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i - 1] + 1 != nums[i]:
            return nums[i - 1] + 1
    return nums[-1] + 1
