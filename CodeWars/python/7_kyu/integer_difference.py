# https://www.codewars.com/kata/57741d8f10a0a66915000001/train/python

def int_diff(lst: list, n: int):
    count = 0
    for i, num1 in enumerate(lst):
        for j in range(i + 1, len(lst)):
            num2 = lst[j]
            if abs(num1 - num2) == n:
                count += 1
    return count