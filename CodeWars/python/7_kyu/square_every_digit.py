# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    values, output = [*str(num)], []
    for x in values:
        output.append(str(int(x) * int(x)))
    return int("".join(output))
