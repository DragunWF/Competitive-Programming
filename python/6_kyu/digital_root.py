# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    values, array = [*str(n)], []
    while True:
        for x in values:
            array.append(int(x))
        if sum(array) <= 9:
            return sum(array)
        result = sum(array)
        values, array = [a for a in str(result)], []
