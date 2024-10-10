# https://www.codewars.com/kata/563cf89eb4747c5fb100001b

def multiply(n):
    return n * 5 ** (len(str(n)) - (1 if n < 0 else 0))
