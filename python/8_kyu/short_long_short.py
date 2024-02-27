# https://www.codewars.com/kata/50654ddff44f800200000007/train/python

def solution(a, b):
    short = a if len(a) < len(b) else b
    long = b if short == a else a
    return f"{short}{long}{short}"
