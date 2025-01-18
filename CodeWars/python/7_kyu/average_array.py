# https://www.codewars.com/kata/596f6385e7cd727fff0000d6/train/python

def avg_array(arrs: list):
    output = [0 for i in range(len(arrs[0]))]
    for arr in arrs:
        for i in range(len(arr)):
            output[i] += arr[i]
    return [n / len(arrs) for n in output]
