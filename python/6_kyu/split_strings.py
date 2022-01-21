# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    interval, iteration, pair = 0, 0, ""
    values, new_set = [*s], []
    for letter in values:
        interval += 1
        iteration += 1
        pair += letter
        if interval == 2:
            new_set.append(pair)
            pair = ""
            interval = 0
        if iteration == len(values) and len(pair) == 1:
            pair += "_"
            new_set.append(pair)
    return new_set
