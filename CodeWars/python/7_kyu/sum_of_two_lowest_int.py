# https://www.codewars.com/kata/558fc85d8fd1938afb000014

def sum_two_smallest_numbers(numbers):
    x = min(numbers)
    numbers.pop(numbers.index(min(numbers)))
    return x + min(numbers)
