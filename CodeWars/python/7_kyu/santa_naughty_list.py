# https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef/train/python

def find_children(santas_list, children):
    output = []
    for child in children:
        if child in santas_list and not child in output:
            output.append(child)
    return sorted(output)