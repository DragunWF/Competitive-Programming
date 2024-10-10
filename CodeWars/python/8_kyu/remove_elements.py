# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2

def remove_every_other(arr):
    return [arr[i] for i in range(len(arr)) if (i + 1) % 2 != 0]
