# https://www.codewars.com/kata/5239f06d20eeab9deb00049b/train/python

def fibonacci(n):
    if n <= 0:
        return []
    seq = [0, 1]
    if n <= len(seq):
        return seq[0:n]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq
