# https://www.codewars.com/kata/5c374b346a5d0f77af500a5a/train/python

def elevator(left, right, call):
    return "left" if abs(left - call) < abs(right - call) else "right"
