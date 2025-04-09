# https://www.codewars.com/kata/5a04133e32b8b998dc000089/train/python

def solve(arr: list[int]) -> list[int]:
    output = []
    n = len(arr)
    for i in range(n):
        is_dominant = True
        for j in range(i + 1, n):
            if arr[i] <= arr[j]:
                is_dominant = False
                break
        if is_dominant:
            output.append(arr[i])
    return output
