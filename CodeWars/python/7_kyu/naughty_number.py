# https://www.codewars.com/kata/679bdbe30a5faf7bbf634e0f/train/python

def naughty_number(matrix: list[int | list]) -> int:
    def contains_number(arr: list) -> bool:
        if len(arr) == 1:
            return contains_number(arr[0]) if type(arr[0]) == list else True
        return False
    for i, arr in enumerate(matrix):
        if contains_number(arr):
            return i
