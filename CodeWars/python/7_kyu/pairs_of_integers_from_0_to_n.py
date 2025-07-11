# https://www.codewars.com/kata/588e27b7d1140d31cb000060/train/python

def generate_pairs(n: int) -> list:
    output = []
    for i in range(0, n + 1):
        for j in range(0, i + 1):
            output.append([j, i])
    output.sort(key=lambda x: (x[0], x[1]))
    return output
