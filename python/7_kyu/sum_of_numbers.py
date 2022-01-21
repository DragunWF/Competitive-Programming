# https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a, b):
    min_x = a if a < b else b
    max_y = a if min_x == b else b
    values = [*range(min_x, max_y + 1)]
    return sum(values)
