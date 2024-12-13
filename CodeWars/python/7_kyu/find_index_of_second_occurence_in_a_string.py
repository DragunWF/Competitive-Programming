# https://www.codewars.com/kata/63f96036b15a210058300ca9/train/python

def second_symbol(s, symbol):
    found_one = False
    for i, char in enumerate(s):
        if char == symbol:
            if found_one:
                return i
            found_one = True
    return -1
