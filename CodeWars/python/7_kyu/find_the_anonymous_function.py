# https://www.codewars.com/kata/55a12bb8f0fac1ba340000aa/train/javascript

from types import FunctionType


def find_function(func, arr):
    anonymous_func = None
    for item in func:
        if isinstance(item, FunctionType):
            anonymous_func = item
            break
    return list(filter(anonymous_func, arr))
