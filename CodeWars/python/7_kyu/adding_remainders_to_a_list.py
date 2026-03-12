# https://www.codewars.com/kata/5acc3634c6fde760ec0001f7/train/python

def solve(nums: list[int], div: int) -> list[int]:
    return [num + (num % div) for num in nums]
