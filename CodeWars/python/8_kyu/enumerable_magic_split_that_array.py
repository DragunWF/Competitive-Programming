# https://www.codewars.com/kata/545b342082e55dc9da000051/train/python

def partition(arr, classifier_method):
    output = ([], [])
    for item in arr:
        output[int(not classifier_method(item))].append(item)
    return output
