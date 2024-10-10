# https://www.codewars.com/kata/5aa1bcda373c2eb596000112/train/python

def max_tri_sum(numbers):
    return sum(sorted(list(set(numbers)), reverse=True)[0:3])
