# https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/python

def smaller(arr):
    output = []
    for i in range(len(arr)):
        count = 0
        for j in range(i, len(arr)):
            if (arr[j] < arr[i]):
                count += 1
        output.append(count)
    return output
