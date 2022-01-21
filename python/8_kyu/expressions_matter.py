# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e

def expression_matter(a, b, c):
    first = a * (b + c)
    second = a * b * c
    third = a + b * c
    fourth = (a + b) * c
    fifth = a + b + c
    values, highest = [first, second, third, fourth, fifth], 0
    for value in values:
        if value > highest:
            highest = value
    return highest
