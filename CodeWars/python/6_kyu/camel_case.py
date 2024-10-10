# https://www.codewars.com/kata/587731fda577b3d1b0001196/python

def camel_case(string):
    return "".join([x.title() for x in string.split(" ")])
