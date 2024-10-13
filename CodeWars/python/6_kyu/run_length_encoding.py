# https://www.codewars.com/kata/546dba39fa8da224e8000467/train/python

def run_length_encoding(s: str) -> list:
    output = []
    prev_char = None
    for char in s:
        if char != prev_char:
            output.append([1, char])
        else:
            output[-1][0] += 1
        prev_char = char
    return output
