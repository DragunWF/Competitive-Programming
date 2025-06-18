# https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055/train/python

def find_array(arr1: list, arr2: list[int]) -> list[int]:
    output = []
    for index in arr2:
        if 0 <= index < len(arr1):
            output.append(arr1[index])
    return output
