# https://www.codewars.com/kata/51f082ba7297b8f07f000001/train/python

def find_in_array(seq, predicate):
    for i in range(len(seq)):
        if predicate(seq[i], i):
            return i
    return -1
