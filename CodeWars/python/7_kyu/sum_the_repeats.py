# https://www.codewars.com/kata/56b4bae128644b5613000037/train/python

def repeat_sum(data: list[list[int]]) -> int:
    seen = set()
    to_sum = set()
    for lst in data:
        for num in set(lst):
            if num in seen:
                to_sum.add(num)
            else:
                seen.add(num)
    return sum(to_sum)
