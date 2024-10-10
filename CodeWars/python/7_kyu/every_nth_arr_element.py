# https://www.codewars.com/kata/5753b987aeb792508d0010e2/train/python

def every(array, interval=None, start_index=None):
    if interval is None and start_index is None:
        return array
    output = []
    for i in range(0 if start_index is None else start_index, len(array), interval):
        output.append(array[i])
    return output
