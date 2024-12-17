# https://www.codewars.com/kata/51dda84f91f5b5608b0004cc/train/python

def solution(number):
    output = [0, 0, 0]
    for i in range(2, number):
        if i % 3 == 0 and i % 5 == 0:
            output[2] += 1
        elif i % 5 == 0:
            output[1] += 1
        elif i % 3 == 0:
            output[0] += 1
    return output
