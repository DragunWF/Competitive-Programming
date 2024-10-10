# https://www.codewars.com/kata/594093784aafb857f0000122/train/python

def diff(a, b):
    a, b = set(a), set(b)
    return sorted(list((a.difference(b)).union(b.difference(a))))
