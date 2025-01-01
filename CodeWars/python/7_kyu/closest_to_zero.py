# https://www.codewars.com/kata/59887207635904314100007b/train/python

def closest(arr: list[int]):
    min_value = min(list(map(abs, arr)))
    if min_value != 0 and min_value in arr and -min_value in arr:
        return None
    return -min_value if -min_value in arr else min_value
