# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    output = []
    for n in range(a, b + 1):
        digital_sum = 0
        for i, s in enumerate(str(n)):
            digital_sum += int(s) ** (i + 1)
        if digital_sum == n:
            output.append(n)
    return output
