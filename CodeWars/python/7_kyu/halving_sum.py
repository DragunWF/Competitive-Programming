# https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d/train/python

def halving_sum(n: int) -> int:
    divisor = 2
    total = n
    while divisor <= n:
        total += n // divisor
        divisor *= 2
    return total
