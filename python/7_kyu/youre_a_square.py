# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

from math import sqrt


def is_square(n):
    if n < 0:
        return False
    square_root = sqrt(n)
    return square_root * square_root == n
