# https://www.codewars.com/kata/585ba66ce08bae791b00011b/train/python

def index_finder(a: list, x) -> int:
    for i in range(1, len(a)):
        if a[i] == x:
            return i
