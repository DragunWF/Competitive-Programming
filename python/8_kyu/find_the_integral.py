# https://www.codewars.com/kata/59811fd8a070625d4c000013/train/python

def integrate(coefficient, exponent):
    N = exponent + 1
    return f"{int(coefficient / N)}x^{N}"
