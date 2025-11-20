# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

def is_pangram(s: str) -> bool:
    return len(set(char for char in s.lower() if char.isalpha())) == 26
