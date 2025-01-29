# https://www.codewars.com/kata/5a092d9e46d843b9db000064/train/python

def solve(arr: list[int]) -> list[int]:
    for n in arr:
        if (n < 0 and not abs(n) in arr) or (n > 0 and not -n in arr):
            return n
