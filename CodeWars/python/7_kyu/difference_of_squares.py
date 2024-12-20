# https://www.codewars.com/kata/558f9f51e85b46e9fa000025/train/python

def difference_of_squares(n: int) -> int:
    square_sum = 0
    sum_of_squares = 0
    for i in range(1, n + 1):
        square_sum += i
        sum_of_squares += i ** 2
    return square_sum ** 2 - sum_of_squares
