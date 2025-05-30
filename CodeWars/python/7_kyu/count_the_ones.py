# https://www.codewars.com/kata/5519e930cd82ff8a9a000216/train/python

def hamming_weight(x: int) -> int:
    return len([digit for digit in bin(x)[2:] if digit == "1"])
