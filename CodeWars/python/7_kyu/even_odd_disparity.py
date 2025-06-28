# https://www.codewars.com/kata/59c62f1bdcc40560a2000060/train/python

def solve(arr: list) -> int:
    even_num_sum = 0
    odd_num_sum = 0
    for num in arr:
        if type(num) == int:
            if num % 2 == 0:
                even_num_sum += 1
            else:
                odd_num_sum += 1
    return even_num_sum - odd_num_sum
