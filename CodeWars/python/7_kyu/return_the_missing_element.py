# https://www.codewars.com/kata/5299413901337c637e000004/train/python

def get_missing_element(seq: list[int]):
    seq.sort()
    if seq[0] != 0:
        return 0
    for i in range(1, len(seq)):
        NEXT_NUM = seq[i - 1] + 1
        if NEXT_NUM != seq[i]:
            return NEXT_NUM
    return seq[-1] + 1
