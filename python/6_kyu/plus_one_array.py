# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9

def up_array(arr):
    if not arr:
        return None
    for n in arr:
        if n > 9 or n < 0:
            return None
    arr = str(int("".join([str(x) for x in arr])) + 1)
    return [int(i) for i in arr]
