# https://www.codewars.com/kata/542ebbdb494db239f8000046/train/python

def next_item(xs: list, item):
    found_item = False
    for element in xs:
        if found_item:
            return element
        if element == item:
            found_item = True
