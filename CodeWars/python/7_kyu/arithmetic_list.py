# https://www.codewars.com/kata/541da001259d9ca85d000688/train/python


def seqlist(first: int, c: int, l: int) -> list[int]:
    seq = []
    n = first
    for i in range(l):
        seq.append(n)
        n += c
    return seq
