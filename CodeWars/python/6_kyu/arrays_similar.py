# https://www.codewars.com/kata/51e704f2d8dbace389000279/train/python

def arrays_similar(seq1: list, seq2: list):
    if len(seq1) != len(seq2):
        return False
    for element in seq1:
        if not element in seq2 or seq1.count(element) != seq2.count(element):
            return False
    return True
