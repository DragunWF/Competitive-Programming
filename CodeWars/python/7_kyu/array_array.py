# https://www.codewars.com/kata/57eb936de1051801d500008a/train/python

def explode(arr):
    output, score = [], 0
    if type(arr[0]) == str and type(arr[1]) == str:
        return "Void!"
    for item in arr:
        if type(item) != str:
            score += item
    for i in range(score):
        output.append(arr)
    return output