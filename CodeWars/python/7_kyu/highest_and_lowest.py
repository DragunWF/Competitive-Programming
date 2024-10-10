# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    x_values = numbers.split()
    x_values = [int(x) for x in x_values]
    return f"{max(x_values)} {min(x_values)}"
