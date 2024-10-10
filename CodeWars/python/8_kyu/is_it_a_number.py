# https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python

def is_digit(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
