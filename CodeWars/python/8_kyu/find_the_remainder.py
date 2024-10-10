# https://www.codewars.com/kata/524f5125ad9c12894e00003f

def remainder(a, b):
    try:
        return a % b if a > b else b % a
    except ZeroDivisionError:
        return
