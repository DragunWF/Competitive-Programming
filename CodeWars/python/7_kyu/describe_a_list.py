# https://www.codewars.com/kata/57a4a3e653ba3346bc000810/train/python

def describe_list(lst):
    if not lst:
        return "empty"
    return "singleton" if len(lst) == 1 else "longer"