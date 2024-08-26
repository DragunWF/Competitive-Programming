# https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python

def largest_pair_sum(numbers: list[int]) -> int:
    numbers.sort()
    return numbers[-1] + numbers[-2]
