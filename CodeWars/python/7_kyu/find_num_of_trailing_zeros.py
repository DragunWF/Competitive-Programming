# https://www.codewars.com/kata/66e793bba4b1a6f2e8f890e5/train/python

def trailing_zeros(n: int) -> int:
    binary = bin(n)[2:]
    trailing_count = 0
    for i in range(len(binary) - 1, -1, -1):
        if binary[i] == "0":
            trailing_count += 1
            continue
        break
    return trailing_count
