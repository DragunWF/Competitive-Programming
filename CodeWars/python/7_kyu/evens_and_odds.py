# https://www.codewars.com/kata/583ade15666df5a64e000058/train/python

def evens_and_odds(n: int) -> str:
    return bin(n)[2:] if n % 2 == 0 else hex(n)[2:]
