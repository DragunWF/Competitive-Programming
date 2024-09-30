# https://www.codewars.com/kata/56bc1acf66a2abc891000561/train/python

from preloaded import greek_alphabet


def greek_comparator(lhs, rhs):
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
