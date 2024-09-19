# https://www.codewars.com/kata/562926c855ca9fdc4800005b/train/python

def number_to_pwr(number, p):
    total = 1
    for i in range(p):
        total *= number
    return total
