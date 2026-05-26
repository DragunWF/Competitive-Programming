# https://www.codewars.com/kata/54599705cbae2aa60b0011a4/train/python

def one(xs: list, f):
    found_one = False
    for element in xs:
        if f(element):
            if found_one:
                return False
            found_one = True
    return found_one
