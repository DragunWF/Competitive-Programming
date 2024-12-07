# https://www.codewars.com/kata/578a8a01e9fd1549e50001f1/train/python

def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length
