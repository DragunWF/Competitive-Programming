# https://www.codewars.com/kata/59590976838112bfea0000fa/train/python

def beggars(values: list[int], n: int) -> list:
    if n == 0:
        return []
    result = [[] for i in range(n)]
    for i, num in enumerate(values):
        result[i % n].append(num)
    return [sum(arr) for arr in result]