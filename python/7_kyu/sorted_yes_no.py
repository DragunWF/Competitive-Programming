# https://www.codewars.com/kata/580a4734d6df748060000045/train/python

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    return "no"
