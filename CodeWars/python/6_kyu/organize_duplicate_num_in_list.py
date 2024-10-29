# https://www.codewars.com/kata/5884b6550785f7c58f000047/train/python

def group(arr: list[int]) -> list:
    indicies = {} # num: index
    output = []
    for num in arr:
        if not num in indicies:
            indicies[num] = len(output)
            output.append([])
        output[indicies[num]].append(num)
    return output