# https://www.codewars.com/kata/54b7c8d2cd7f51a839000ebf/train/python

def process_array(arr, callback):
    for i in range(len(arr)):
        arr[i] = callback(arr[i])
    return arr