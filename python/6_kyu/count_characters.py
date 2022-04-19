# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(string):
    output = {}
    for c in string:
        output[c] = output[c] + 1 if c in output else 1
    return output


print(count("aba"))
