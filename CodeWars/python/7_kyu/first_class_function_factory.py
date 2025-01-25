# https://www.codewars.com/kata/563f879ecbb8fcab31000041/train/python

def factory(x: int):
    def helper(arr: list[int]) -> list[int]:
        output = []
        for num in arr:
            output.append(num * x)
        return output
    return helper
