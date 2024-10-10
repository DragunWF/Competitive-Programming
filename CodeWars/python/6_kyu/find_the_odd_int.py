# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    values, hgs, intg = {}, 0, None
    for x in seq:
        values[x] = 1 if x not in values else values[x] + 1
    for number in values:
        if values[number] > hgs and (values[number] % 2 >= 1):
            intg, hgs = number, values[number]
    return intg
