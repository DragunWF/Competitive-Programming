# https://www.codewars.com/kata/57f3996fa05a235d49000574/train/python

def abundant(h: int):
    proper_divisors = []
    for i in range(h, 1, -1):
        for j in range(2, i):
            if i % j == 0:
                proper_divisors.append(j)
        total = sum(proper_divisors)
        if total > h:
            return [[i], [total - h]]
    return [[], []]


print(abundant(15))
