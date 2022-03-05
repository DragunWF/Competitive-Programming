# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    count = 0
    while n > 9:
        n = eval("*".join([*str(n)]))
        count += 1
    return count
