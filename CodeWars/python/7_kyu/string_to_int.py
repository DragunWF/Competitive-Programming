# https://www.codewars.com/kata/54fdadc8762e2e51e400032c/train/python

def my_parse_int(strn):
    try:
        return int(strn)
    except ValueError:
        return "NaN"
