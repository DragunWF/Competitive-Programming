# https://www.codewars.com/kata/56aed32a154d33a1f3000018/train/python

def my_first_kata(a,b):
    if not type(a) is int or not type(b) is int: 
        return False
    return a % b + b % a