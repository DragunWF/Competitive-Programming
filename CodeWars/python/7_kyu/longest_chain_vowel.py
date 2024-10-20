# https://www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python

def solve(s: str) -> str:
    vowels = "aeiou"
    longest_chain, current_chain = 0, 0
    for char in s:
        if char in vowels:
            current_chain += 1
        else:
            if current_chain > longest_chain:
                longest_chain = current_chain
            current_chain = 0
    return max(longest_chain, current_chain)
