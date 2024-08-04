# https://www.codewars.com/kata/57a6633153ba33189e000074/train/python

def ordered_count(inp):
    counter = {}
    for char in inp:
        if not char in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    output = []
    for key, value in counter.items():
        output.append((key, value))
    return output
