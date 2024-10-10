# https://www.codewars.com/kata/529872bdd0f550a06b00026e/train/python

def greatest_product(st):
    max_product = 0
    for i in range(len(st) - 4):
        product = 1
        for j in range(i, i + 5):
            product *= int(st[j])
        if product > max_product:
            max_product = product
    return max_product
