# https://www.codewars.com/kata/56044de2aa75e28875000017/train/python

def compound_array(a: list, b: list) -> list:
    output = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            output.append(a[i])
        if i < len(b):
            output.append(b[i])
    return output
