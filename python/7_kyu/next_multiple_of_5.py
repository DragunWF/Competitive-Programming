# https://www.codewars.com/kata/55d1d6d5955ec6365400006d

def round_to_next5(n):
    while n % 5 != 0:
        n += 1
    return n