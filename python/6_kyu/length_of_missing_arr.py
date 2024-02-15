# https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611/train/python

def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0
    lengths = sorted([len(arr if arr != None else []) for arr in array_of_arrays])
    for i, length in enumerate(lengths):
        if not length:
            return 0
        if i + 1 != len(lengths) and length + 1 != lengths[i + 1]:
            return length + 1
